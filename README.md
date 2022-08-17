#  The Crazy Turtle Card Game Solver

[![python versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/)
![os platforms](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-blue)

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/pjd199/crazy_turtle/Test)

[![GitHub](https://img.shields.io/github/license/pjd199/advent_of_code_python?color=black)](./license.md) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

![Crazy Turtle Card Game box](public/images/box.jpeg)

The aim of the game is to arrange the 9 cards so that all the heads
and tails are matching. Sounds simple, apart from there are 23 billion
permutations and only two valid solutions. We own the 1979 version of
the game, and unsurprisingly, had never found a solution.

![Example game board](public/images/board.jpeg)

## Algorithm

The solver uses a depth first approach to finding solutions. For each
permutation of the 9 cards in a 3x3 grid, the solver starts in the top
left, rotating the top middle card until it matches, then starts rotating 
the top right card to find an match, and so forth until the bottom right
card matches - at which a solution is declared. Only successful permuations
and rotations sequences are continued, with other paths ignored to reduce
the search space.

The solver algorithm generates 16 solutions, which are the four solutions
viewed from the 4 angles of rotation. Of these four solutions, two are
repeats, since two cards in the game are identical. When all these
duplicates are removed, the game has just two solutions.

With the help of Python's multiprocessing Pool, the solver finds the 
two solutions in around 5 seconds.

## Installation

Clone the repo
```
git clone https://github.com/pjd199/crazy_turtle
```

## Usage

From the command line, run
```
python crazy_turtle.py
```
```
Solving The 'Crazy Turle' Game
................
Found 2 unique solutions in 5.30s.

Solution 1
['RH', 'OH', 'RT', 'BT'] : ['GH', 'BH', 'RT', 'OT'] : ['RH', 'OH', 'GT', 'BT']
['RH', 'GH', 'BT', 'OT'] : ['RH', 'BH', 'OT', 'GT'] : ['GH', 'RH', 'OT', 'BT']
['BH', 'GT', 'OT', 'GH'] : ['OH', 'RT', 'BT', 'GH'] : ['OH', 'GT', 'BT', 'RH']

Solution 2
['OH', 'RT', 'BT', 'RH'] : ['OH', 'GT', 'BT', 'RH'] : ['RH', 'OT', 'BT', 'GH']
['BH', 'GT', 'OT', 'GH'] : ['BH', 'RT', 'OT', 'GH'] : ['BH', 'OT', 'GT', 'RH']
['OH', 'GT', 'BT', 'RH'] : ['OH', 'RT', 'BT', 'GH'] : ['GH', 'BT', 'OT', 'RH']
key:
colours   - Orange, Green, Brown, Red
body part - Head, Tail
```

## Test

From the command line, run
```
pytest test_crazy_turtle.py
```

## Solutions

### First Solution

![First solution](public/images/solution1.jpeg)

### Second Solution

![Second solution](public/images/solution2.jpeg)

## Licence

Solver distributed under the MIT License. See [LICENCE.md](LICENSE.md) for more information.

## Author

Pete Dibdin