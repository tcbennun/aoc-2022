elves = [0]
for line in open("day1.txt"):
    line = line.strip()
    if not len(line):
        elves.append(0)
    else:
        elves[-1] += int(line)

print(max(elves))

tot = 0
for _ in range(3):
    m = max(elves)
    tot += m
    elves.remove(m)

print(tot)
