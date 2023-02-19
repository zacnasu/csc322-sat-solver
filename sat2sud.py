import sys

import fileinput
for line in fileinput.input(encoding="utf-8"):

if !sys.argv[0]:
    raise Exception("no file to read")

file = open(sys.argv[0], "r")

if file.readline().upper() == "UNSAT":
    exit(0)

