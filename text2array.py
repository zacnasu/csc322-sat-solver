import sys

# Read puzzle from stdin
#0:81 is the index first 9 x 9 puzzle from the
puzzle_str = ''.join((sys.stdin.read().split('\n')))[0:81]

size = 9

#Convert puzzle string to a 2D array
puzzle = [[int(puzzle_str[i + j * size]) if puzzle_str[i + j * size].isdigit() else 0 for i in range(size)] for j in
          range(size)]

# Print the puzzle as a 2D array
#for row in puzzle:
    #print(row)
