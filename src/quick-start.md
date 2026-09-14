# Quick Start

To quickly get started with FrameX we recommend using FrameX-Workbench. This allows quick and easy tinkering with the logic engine and the features.

## The example

Copy this complete program — four statements, including the world declaration: a world assumption, a fact, a rule, and a question:

```framex
world open.
socrates:Human.
?X:Mortal <- ?X:Human.
?- socrates:Mortal.
```

Read it aloud: Socrates is a human. A person is mortal if that person is
human. Is Socrates mortal? The answer is `true`. Every statement ends with
a period; `?X` is a variable and `world open.` declares the world
assumption (see [World Assumption](./syntax/world-assumption.md)).

## Option 1: FrameX-Workbench

To get started using FrameX we recommend using the [FrameX-Workbench](https://framex.nlp-lab.ai/). After a quick login you can start modeling the logic directly in the web-tool. You can find FrameX-Workbench here: https://framex.nlp-lab.ai/.

1. Login to [framex.nlp-lab.ai](https://framex.nlp-lab.ai/). *If you dont have a user, please reach out to the Teaching Assistants.*
2. Start the Workspace using the *Start Workspace* button on the top right.
3. Create a new file using the *New file* button in the *FILES* tab on the left side of the screen and name it `quick-start.fx`. If its not visible, you may need to click *Show files* first to show the colapsed *FILES* section. 
4. Write your FrameX F-Logic code in the created file. You can use the example from above to start tinkering. 
5. Save the file and press *Run program* on the top right to evaluate the file.
6. The result shows the logical answer (`true`); execution status is reported separately.

## Option 2: FrameX-CLI

As an alternative to the [FrameX-Workbench](https://framex.nlp-lab.ai/) you can also run and validate FrameX F-Script using FrameX-CLI locally on your machine. The CLI will be available soon on GitHub.

1. Name the file `quick-start.fx`.
2. Run it from a terminal:
```bash
framex run quick-start.fx
```
3. Add `expect true: socrates:Mortal.` to your file, then run the test:
```bash
framex test quick-start.fx
```

## Next Steps
Congrats! You have created and run your first FrameX program. 🎉🎉🎉 

To go deeper in the 🐇-hole and learn more, we recommend doing the [Tutorial](./tutorial/index.md).
