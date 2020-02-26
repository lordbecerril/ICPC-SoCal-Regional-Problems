import sys

lines = []

for line in sys.stdin:
    print (line)
    line = line.strip()
    if line:
        lines.append(line)
