import re
import sys
import statistics

cpu_stat = []
restarts = []
conflicts = []
decisions = []
propagations = []
conflict_literals = []
memory_used = []
line = sys.stdin.readline()
while line:
    if 'CPU time' in line:
        matches = re.findall(r'\d+\.\d+', line)
        if matches:
            cpu_stat.append(float(matches[0]))
    if 'restarts' in line:
        matches = re.findall(r'\d+', line)
        if matches:
            restarts.append(float(matches[0]))
    if 'conflicts' in line:
        matches = re.findall(r'\d+', line)
        if matches:
            conflicts.append(float(matches[0]))
    if 'decisions' in line:
        matches = re.findall(r'\d+', line)
        if matches:
            decisions.append(float(matches[0]))
    if 'propagations' in line:
        matches = re.findall(r'\d+', line)
        if matches:
            propagations.append(float(matches[0]))
    if 'conflict literals' in line:
        matches = re.findall(r'\d+', line)
        if matches:
            conflict_literals.append(float(matches[0]))
    if 'Memory used' in line:
        matches = re.findall(r'\d+\.\d+', line)
        if matches:
            memory_used.append(float(matches[0]))
    line=sys.stdin.readline()

print('Cpu time')
print("mean: "+ str(statistics.mean(cpu_stat)))
print("greatest: "+ str(max(cpu_stat)))
print("lowest: " + str(min(cpu_stat)))

print('restarts')
print("mean: "+ str(statistics.mean(restarts)))
print("greatest: "+ str(max(restarts)))
print("lowest: " + str(min(restarts)))

print('conflicts')
print("mean: "+ str(statistics.mean(conflicts)))
print("greatest: "+ str(max(conflicts)))
print("lowest: " + str(min(conflicts)))

print('decisions')
print("mean: "+ str(statistics.mean(decisions)))
print("greatest: "+ str(max(decisions)))
print("lowest: " + str(min(decisions)))

print('propagations')
print("mean: "+ str(statistics.mean(propagations)))
print("greatest: "+ str(max(propagations)))
print("lowest: " + str(min(propagations)))

print('conflict literals')
print("mean: "+ str(statistics.mean(conflict_literals)))
print("greatest: "+ str(max(conflict_literals)))
print("lowest: " + str(min(conflict_literals)))

print('memory_used')
print("mean: "+ str(statistics.mean(memory_used)))
print("greatest: "+ str(max(memory_used)))
print("lowest: " + str(min(memory_used)))