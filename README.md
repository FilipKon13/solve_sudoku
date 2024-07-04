# Solve Sudoku with code

Quick simple project solving sudoku available at sudoku.com website. Made mainly to play around with computer vision, simple CNNs and learn to create C bindinds for Python.

## How to use it

It depends. If you have similar-enough setup and trust my `digit_model.h5` then it should work out-of-the-box, just run `main.py` script while having open sudoku.com website with Chrome browser. Have sudoku visible on your screen and then press anything on your keyboard (I personally use shift). Sudoku should be solved in some time, you can trace progress using log messages. Then, press again, to load new game. Wait till whole sudoku is visible and repeat.

If not, then you may have to do some adjustments.

- If you do not trust my `digit_model.h5` file (see [here](https://github.com/tensorflow/models/security/policy)) you can train the model youself by running `cnn.py` script - all dataset is in `pictures` directory,
- Window coordinatess - `SUDOKU_REC` variable specifies rectangle where sudoku is located on screen. You can adjust it/verify it works by using `get_image(True)` function from `util.py` - it saves the screenshot to png file,
- Image resolution - neural network and capturing function assume that whole sudoku has dimensions 528 by 528 pixels. If it has not, then you need to change appropriate constant in `util.py` and train neural network in `cnn.py`.

You can also run this in manual mode, when you can place sudoku on standard input and program wil solve it (usefull if network makes singular mistakes, you can correct single digits manually).

## How to go faster

With harder puzzles you may notice that it takes a while to figure out solution, even after capturing and parsing what's going on on the screen. Well, it's because sudoku-solving function is really basic backtrack and its written in Python (look at `solve_sudoku_py.py` file).

I wanted to do something with C bindings (and to go faster), so there is similar logic implemented in C in `solve.c` and bindings created in `solve_sudoku_c.py` file. To use it you need to compile `solve.c` to shared library (I did not posted binary on repo - do NOT trust binaries in random repos).

Provided `Makefile`, `solve.c` and `solve_sudoku_c.py` files were prepared for Windows machines (Windows + WSL here - pynput does not work well on WSL's side of the things on my version). To run this on diffent OS, you need to change extensions/loading strategies accordingly e.g. for Linux, changing `.dll` to `.so` (canonical shared library extension) in both files and using appropriate calling convention in `solve.c` should be enough.

## How it was done

Dataset was prepared using methods in `prep_data.py` script. Screenshots from ~100 puzzles were captured and partitioned into singular tiles. Then, I manually sorted around 100 images of every type (i.e. empty square + 9 types of number squares) and trained neural network on it. Then I used mentioned network to assing labels to rest of images and verified that everything indeed has correct label (it had not, there were couple 5's and 8's with label '6').

Final model was trained on full dataset and so far it did not make a single mistake while running `main.py` script.

### Quick digression about Data Augmentation

I could use these 100 manually labeled samples and use techniques from Data Augmentation department to make bigger dataset. However, given how standarized input to this network is going to be (literally every digit is same every time, modulo position, shade of color and sometimes dividing lines are visible), I decided to train the network just for this particular task.

## Result

Well, it works. On harder instances (read: more empty squares) Python version of solver may struggle, so it takes few seconds to find a solution. However, with C version most of the time is spend capturing the screen and preparing it to send to network (TODO: use something faster than ImageGrab from Pillow).

Single iteration, i.e. parsing table + solving sudoku ('hard' instance) takes less than a second on my machine, most of which is taken by mentioned ImageGrab and partition into squares:

| Functionality      | Time      |
| ------------- | ------------- |
| Screenshot + partition | 0.8544s |
| Neural Network | 0.1141s |
| Solving | 0.0149s |
| In total | 0.9834s |

There is definitely room for improvement (e.g. capturing faster, smaller NN), but at the moment even putting numbers into browser takes significant time in comparison.
