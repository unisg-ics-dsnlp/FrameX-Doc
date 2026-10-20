#!/usr/bin/env python3
"""Check executable documentation against an installed FrameX 0.4.4, offline."""

import argparse
import difflib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src"


def truth(status):
    return {"status": status}


def bindings(*rows):
    return {"status": "bindings", "bindings": list(rows)}


# Expected query answers are independent of the listings' expect statements.
TUTORIAL_QUERIES = {
    "01": [truth("true")],
    "02": [bindings({"Mother": "sarah", "Son": "isaac"})],
    "03": [bindings({"Child": "benjamin"}, {"Child": "joseph"}), truth("true")],
    "04": [truth("true"), truth("true")],
    "05": [bindings({"Child": "benjamin"}, {"Child": "joseph"})],
    "06": [truth("true")],
    "07": [bindings({"Grandfather": "abraham"})],
    "08": [bindings({"Ancestor": "rebekah"}, {"Ancestor": "sarah"})],
    "09": [truth("unknown"), bindings({"Paper": "p2"})],
    "10": [truth("true")],
    "11": [bindings({"Step": "step1"}, {"Step": "step2"}), bindings({"Next": "step2"})],
    "12": [truth("true")],
    "13": [bindings({"Property": "father", "Value": "abraham"},
                    {"Property": "label", "Value": '"Isaac"'}),
           bindings({"Class": "`Person`"})],
    "14": [truth("true")],
    "15": [truth("unknown")],
}


def blocks(page, language):
    return re.findall(r"```" + re.escape(language) + r"\n(.*?)```",
                      page.read_text(encoding="utf-8"), re.S)


def normalized(answer):
    answer = dict(answer)
    if "bindings" in answer:
        answer["bindings"] = sorted(answer["bindings"], key=lambda row: json.dumps(row, sort_keys=True))
    return answer


def check_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}\nExpected: {expected!r}\nActual:   {actual!r}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", default=os.environ.get("FRAMEX_BINARY", "framex"))
    args = parser.parse_args()
    located = shutil.which(args.binary)
    if not located:
        parser.error("framex not found; install the engine or pass --binary /absolute/path/to/framex")
    binary = str(Path(located).resolve())
    try:
        import framex.tools  # noqa: F401 - fail early when the host is unavailable
    except ImportError:
        parser.error("install the FrameX Python package, or set PYTHONPATH to framex-core/python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", FRAMEX_BINARY=binary,
               PATH=str(Path(binary).parent) + os.pathsep + os.environ.get("PATH", ""))
    checks = 0

    with tempfile.TemporaryDirectory(prefix="framex-doc-check-") as directory:
        temp = Path(directory)

        def run(*command, cwd=temp):
            result = subprocess.run(command, cwd=cwd, env=env, text=True,
                                    capture_output=True, timeout=60)
            if result.returncode:
                raise AssertionError(f"Command failed: {command!r}\n{result.stdout}\n{result.stderr}")
            return result.stdout

        def report(*files, queries=None):
            data = json.loads(run(binary, "report", *(str(file) for file in files)))
            check_equal(data["failed"], 0, "expectations")
            if queries is not None:
                check_equal([normalized(item["answer"]) for item in data["queries"]],
                            [normalized(answer) for answer in queries], "query answers")
            return data

        print(run(binary, "--version").strip())
        lessons = sorted((SOURCE / "tutorial").glob("lesson-*.md"))
        check_equal(len(lessons), len(TUTORIAL_QUERIES), "tutorial lesson coverage")
        for page in lessons:
            listings = blocks(page, "framex")
            check_equal(len(listings), 1, f"{page.name}: one complete listing")
            file = temp / (page.stem + ".fx")
            file.write_text(listings[0], encoding="utf-8")
            report(file, queries=TUTORIAL_QUERIES[page.name[7:9]])
            checks += 1
        print("PASS: 15 tutorial query/expectation checks")

        family = temp / "family-tree.fx"
        family.write_text(blocks(SOURCE / "examples/family-tree.md", "prolog")[-1], encoding="utf-8")
        report(family, queries=[bindings({"G": "elena"}), bindings({"U": "bruno"}),
                                bindings({"C": "felix"})])
        checks += 1
        for name, language in [("namespaces-identity", "prolog"), ("external-requests", "framex")]:
            file = temp / (name + ".fx")
            file.write_text(blocks(SOURCE / f"syntax/{name}.md", language)[0], encoding="utf-8")
            report(file)
            checks += 1

        programs = SOURCE / "examples/programs"
        for fixture in sorted(programs.glob("grounded-extraction.*.test.fx")):
            data = report(programs / "grounded-extraction.fx", fixture)
            if not data["passed"]:
                raise AssertionError(f"No expectations in {fixture.name}")
            checks += 1
        print("PASS: family, syntax and three extraction receipt scenarios")

        # Each solution has its own directory: save_replay intentionally refuses overwrites.
        for page in sorted((SOURCE / "python-exercise").glob("task-0[2-8]-*.md")):
            work = temp / page.stem
            work.mkdir()
            expected = re.search(r"Running it prints:\n\n```text\n(.*?)```",
                                 page.read_text(encoding="utf-8"), re.S)[1].strip()
            actual = run(sys.executable, "-c", blocks(page, "python")[0], cwd=work).strip()
            if actual != expected:
                difference = "\n".join(difflib.unified_diff(expected.splitlines(), actual.splitlines(),
                                                          fromfile="documented", tofile="actual"))
                raise AssertionError(f"{page.name}\n{difference}")
            checks += 1
        print("PASS: seven Python exercise solutions match documented output")

        receipt = temp / "tool-query.receipts.fx"
        run(sys.executable, "-m", "framex.tools", str(programs / "tool-query.fx"),
            "--binary", binary, "--receipts-out", str(receipt))
        report(programs / "tool-query.fx", receipt, queries=[truth("true")])
        checks += 1

        dialogue_page = SOURCE / "python/dialogue.md"
        flow = temp / "certificate.flow"
        flow.write_text(blocks(dialogue_page, "text")[0], encoding="utf-8")
        answers = temp / "certificate-answers.json"
        answers.write_text(blocks(dialogue_page, "json")[0], encoding="utf-8")
        out = temp / "certificate-run"
        run(sys.executable, "-m", "framex.dialogue", str(flow), "--script", str(answers),
            "--binary", binary, "--output", str(out))
        summary = json.loads((out / "summary.json").read_text(encoding="utf-8"))
        check_equal(summary["status"], "completed", "scripted dialogue")
        checks += 1
        print("PASS: tool-query episode/replay and scripted dialogue; no model calls")

    print(f"{checks} documentation checks passed.")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
