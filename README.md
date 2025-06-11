# MachineLearning
A project for school where I make a program differentiate between Super Mario Galaxy (1 or 2) &amp; Super Mario Odyssey through machine learning techniques. This has no pratical use beyond me wanting to learn about machine learning a bit using two of my favorite games.

This project employs supervised learning, meaning the model recognizes patterns through tagged datasets. Once trained, the model should be able to differentiate between the games.

My dataset consists of two classes, Super Mario Galaxy (1 & 2) and Super Mario Odyssey. The images were sourced from the Super Mario Wiki using the Download All Images Chrome Extension, a Deep Search level of 2, many filters, and a lot of patience. There's a total of roughly 4k images between both classes. No fanart is used, and I do not own any images.

The dataset was split into 80% training and 20% testing, the division was done manually.

## Disclaimer
There was a bug when pushing to GitHub when making the second model, due to attempting to upload the model file, the connection was severed. Some commits were lost in regards to the second model, but the files were backed up to document the process.

which_mario.ipynb is the first model, was replaced with model 2 in a commit after the connection severed.
which_mario_model2.ipynb &amp; which_mario_test.ipynb are the second model.
which_mario_finale.ipynb &amp; which_mario_test_finale.ipynb are the third model.
