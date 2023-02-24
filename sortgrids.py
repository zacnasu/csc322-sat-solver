import sys

for i in range(1, 51):
    line1 = sys.stdin.readline()
    if not ('Grid' in line1):
        print(line1)
        raise Exception("no grid in" + str(i))
    puzzle = []
    for j in range(0,9):
        puzzle.append(sys.stdin.readline())
    f = open('puzzle'+str(i)+'.txt', 'w')
    f.write("".join(puzzle).replace("\n", ""))
    f.close()
