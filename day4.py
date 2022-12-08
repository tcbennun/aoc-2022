import re

tot = 0
for line in open("day4.txt"):
    n0, n1, m0, m1 = (int(n) for n in re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups())
    tot += (n0 <= m0) and (n1 >= m1) or (n0 >= m0) and (n1 <= m1)

print(tot)

tot = 0
for line in open("day4.txt"):
    n0, n1, m0, m1 = (int(n) for n in re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups())
    tot += (m1 < n0) == (n1 < m0)

print(tot)
