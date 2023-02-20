import sys

def main(): 
    # Read puzzle from stdin
    puzzle_str = sys.stdin.read().strip()

    # Convert puzzle string to a 2D array
    puzzle = [[int(puzzle_str[i + j*9]) if puzzle_str[i + j*9].isdigit() else 0 for i in range(9)] for j in range(9)]

    solve(puzzle)
    
def v(i, j, d): 
    return 81 * (i - 1) + 9 * (j - 1) + d

#Reduces Sudoku problem to a SAT clauses 
def sudoku_clauses(): 
    res = []
    # for all cells, ensure that the each cell:
    for i in range(1, 10):
        for j in range(1, 10):
            # denotes (at least) one of the 9 digits (1 clause)
            res.append([v(i, j, d) for d in range(1, 10)])
            # does not denote two different digits at once (36 clauses)
            for d in range(1, 10):
                for dp in range(d + 1, 10):
                    res.append([-v(i, j, d), -v(i, j, dp)])

    def valid(cells): 
        for i, xi in enumerate(cells):
            for j, xj in enumerate(cells):
                if i < j:
                    for d in range(1, 10):
                        res.append([-v(xi[0], xi[1], d), -v(xj[0], xj[1], d)])

    # ensure rows and columns have distinct values
    for i in range(1, 10):
        valid([(i, j) for j in range(1, 10)])
        valid([(j, i) for j in range(1, 10)])
        
    # ensure 3x3 sub-grids "regions" have distinct values
    for i in 1, 4, 7:
        for j in 1, 4 ,7:
            valid([(i + k % 3, j + k // 3) for k in range(9)])
      
    assert len(res) == 81 * (1 + 36) + 27 * 324
    return res

def solve(grid):
    #solve a Sudoku problem
    clauses = sudoku_clauses()
    for i in range(0, 9):
        for j in range(0, 9):
            d = grid[i][j]
            # For each digit already known, a clause (with one literal). 
            if d:
                clauses.append([v(i+1,j+1, d)])

    outputStr = "p cnf " + "729 " + str(len(clauses)) + "\n"
    
    for i, clause in enumerate(clauses):
        for j, num in enumerate(clause):
            if j != len(clause) -1:
                outputStr += str(num) + " "
            else:
                outputStr += str(num) + " 0"
        if i != len(clauses)-1:
            outputStr += "\n"
    print(outputStr)


if __name__ == '__main__':
    from pprint import pprint
    main()