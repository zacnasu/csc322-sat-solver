import sys

# Read puzzle from stdin
puzzle_str = sys.stdin.readline().strip()

# Convert puzzle string to a 2D array
puzzle = [[int(puzzle_str[i + j*9]) if puzzle_str[i + j*9].isdigit() else 0 for i in range(9)] for j in range(9)]

# Print the puzzle as a 2D array
#for row in puzzle:
    #print(row)

#print(puzzle)