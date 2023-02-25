# csc322-sat-solver

Zachary Nasu V00911790\
Chloe Blankers V00917921\
William McCulloch V00896197

This is an implentation of a SAT-Solver for sudoku puzzles.  It is written in python3 with a bash shell scipt wrapper to fit the specifications of the project.

The following is broken up into four sections, the original task, extended task 1, extended task 2, and extended task 3.

## Original task
For the original task we used the following files
1. sud2sat
2. sud2sat.py
3. sat2sud
4. sat2sud.py

To run the code, add a sudoku puzzle into a file puzzle.txt and run the following commands

```
$ ./sud2sat <puzzle.txt >puzzle.cnf
$ minisat puzzle.cnf assign.txt >stat.txt
$ ./sat2sud <assign.txt >solution.txt
$ cat solution.txt
```

If the puzzle is unsatisfiable, sat2sud will output nothing to stdout.

## Extended task 1
For extended task 1 the following files are used:
1. sud2sat1
2. sud2sat1.py
3. top95.txt


**For extended task 1, the code is structured quite differently.**  There is a file called `top95.txt` that contains 95 sudoku puzzles.  When `sud2sat1` is run as a shell script, it runs `sud2sat1.py` where it will read each puzzle and instead of outputting to stdout, it will write the cnf from each puzzle to its own file `top${i}.cnf` where i is the puzzle number. The shell script then runs minisat on each puzzle's cnf and writes each output to `assign${i}.txt` and pipes the performance statistics to `top95stat.txt`.

To run extended task 1
```
$ ./sud2sat3 <top95.txt
```


## Extended task 2
Extended task 2 uses the following files:
1. sud2sat2
2. sud2sat2.py

The code for extended task 2 can be run simililarly to the code for the original task and sat2sud can be reused.
```
$ ./sud2sat2 <puzzle.txt >puzzle.cnf
$ minisat puzzle.cnf assign.txt >stat.txt
$ ./sat2sud <assign.txt >solution.txt
$ cat solution.txt
```

## Extended task 3

Extended task 3 uses the following files:
1. sud2sat3
2. sud2sat3.py

The code for extended task 3 can be run simililarly to the code for the original task and extended task 2. Additionally, sat2sud can be reused.
```
$ ./sud2sat3 <puzzle.txt >puzzle.cnf
$ minisat puzzle.cnf assign.txt >stat.txt
$ ./sat2sud <assign.txt >solution.txt
$ cat solution.txt
```
