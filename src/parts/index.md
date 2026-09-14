# Parts of FrameX

FrameX has a small ecosystem of different tools and parts. Here is an overview of the parts:

## FrameX-UI

FrameX-UI is a webhosted version where one can quickly get started with FrameX. It allows to tinker around and learn the logic without installing a tool on your system.

## FrameX-CLI

The FrameX CLI is a live, terminal-based session on the FrameX reasoning engine. Instead of edit-save-run cycles, you build and probe a knowledge base line by line: every input is applied immediately and becomes the session state.

It supports four kinds of work:
- **Building knowledge:** declare a world assumption (world open. / world closed.), add facts and rules one line at a time, or load whole program files.
- **Asking and inspecting:** run queries (?- ...) for bindings or true/false/unknown answers, explain how a fact was derived, and view session statistics or what the last input changed.
- **Revising safely:** retract facts with automatic recomputation, list what depends on a fact before touching it, and switch world assumptions with the resulting change shown as a diff.
- **Managing the session:** reset with a fresh shell, export the typed commands to the clipboard as a reusable prototype script, and list all commands from the built-in help.

For efficient typing it offers command history (Up/Down), Tab completion of command names, Ctrl-C to cancel a line and Ctrl-D to exit. Shell commands work with or without a leading slash. Everything runs offline from a single binary with no installation step.

## Hackable-FrameX

The Hackable-FrameX is a version of [FrameX-Engine](#framex-engine) that you can extend, tinker and build on top of it. It will be provided in the near future.

## FrameX-Engine

FrameX-Engine is the core engine where FrameX is build apon.

## FrameX-Doc

FrameX-Doc is the documentation of the FrameX ecosystem and tooling. You are currently reading it.

Its based on [mdBook](https://github.com/rust-lang/mdBook) and you can find the source-code on [GitHub FrameX-Doc](https://github.com/unisg-ics-dsnlp/FrameX-Doc).

Feel free to create a PR or open a Issue if anything is missing or wrong.
