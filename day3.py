tot = 0
for line in open("day3.txt"):
    line = line.strip()
    n = len(line) // 2
    s = list(set(line[:n]).intersection(set(line[n:])))[0]
    tot += ord(s) - (ord("A") - 27, ord("a") - 1)[s.islower()]

print(tot)

tot = 0
ss = [None] * 3
for i, line in enumerate(open("day3.txt")):
    j = i % 3
    ss[j] = set(line.strip())
    if j == 2:
        s = list(ss[0].intersection(ss[1]).intersection(ss[2]))[0]
        tot += ord(s) - (ord("A") - 27, ord("a") - 1)[s.islower()]

print(tot)
