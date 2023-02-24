import sys

def value(i, j, k): 
    return 81 * (i - 1) + 9 * (j - 1) + (k - 1) + 1

def get_clauses(): 
    clauses = []
    for i in range(1, 10):
        for j in range(1, 10):
            # denotes (at least) one of the 9 digits (1 clause)
            clauses.append([value(i, j, d) for d in range(1, 10)])
    
    for d in range(1, 10):
        # each element in each row has distinct 1-9 value
        for i in range(1, 10):
            for j1 in range(1, 10):
                for j2 in range(j1+1, 10):
                    clauses.append([-value(i, j1, d), -value(i, j2, d)])
        #each element in each column has distinct 1-9 value
        for j in range(1, 10):
            for i1 in range(1, 10):
                for i2 in range(i1+1, 10):
                    clauses.append([-value(i1, j, d), -value(i2, j, d)])

    # each element in grid has distinct 1-9 value
    for d in range(1, 10):
        for i in [1,4,7]:
            for j in [1,4,7]:
                for k1 in range(9):
                    for k2 in range(k1+1, 9):
                        clauses.append([-value(i+(k1%3), j+(k1//3), d), -value(i+(k2%3), j+(k2//3), d)])
    
    for d1 in range(1, 10):
        for d2 in range(1, 10):
            for i in range(1, 10):
                for j in range(1, 10):
                    if d1 < d2:
                        clauses.append([-value(i, j, d1), -value(i, j, d2)])
    
    # If we desired to delete duplicate clauses
    # indexes_to_delete = []
    # for i in range(0, len(res)):
    #     for j in range(i + 1, len(res)):
    #         if sorted(res[i]) == sorted(res[j]):
    #             indexes_to_delete.append(j)
    # indexes_to_delete.sort()
    # if indexes_to_delete:
    #     for x in reversed(indexes_to_delete):
    #         del res[x]
    return clauses

if __name__ == '__main__':
    # Read puzzle from stdin
    puzzle_str = sys.stdin.read().replace(" ", "").replace("\n", "")

    # Convert puzzle string to a 2D array
    puzzle = [[int(puzzle_str[i + j*9]) if puzzle_str[i + j*9].isdigit() else 0 for i in range(9)] for j in range(9)]
    clauses = get_clauses()
    for i in range(0, 9):
        for j in range(0, 9):
            d = puzzle[i][j]
            # For each digit already known, a clause (with one literal). 
            if d != 0:
                clauses.append([value(i+1,j+1, d)])

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
