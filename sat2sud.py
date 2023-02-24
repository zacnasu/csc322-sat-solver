import sys


def main():

    file = sys.stdin.read().split('\n')
    firstLine = file[0]
    secondLine = file[1]
    if "UNSAT" in firstLine:
        exit(0)
    else:
        sol = secondLine.split()
        sol = sol[:-1]
        sol = [eval(x) for x in sol]
        solve(sol)


def value(i, j, d):
    return 81 * (i - 1) + 9 * (j - 1) + d


def solve(sol):

    output = ""

    def read_cell(i, j):
        for d in range(1, 10):
            if value(i, j, d) in sol:
                return d

    for i in range(1, 10):
        n = 0
        for j in range(1, 10):
            n += 1
            output += str(read_cell(i, j))
            if n % 3 == 0 and n != 9:
                output += ' '
        output += '\n'

    print(output[:-1])


if __name__ == '__main__':
    main()
