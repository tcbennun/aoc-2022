tot = 0
for line in open("day2.txt"):
    n = ord(line[0]) - ord("A")
    m = ord(line[2]) - ord("X")
    tot += 1 + m + ((m - n) % 3 + 1) % 3 * 3

print(tot)

tot = 0
for line in open("day2.txt"):
    n = ord(line[0]) - ord("A")
    x = ord(line[2]) - ord("X")
    m = (n + (x + 2) % 3) % 3
    tot += 1 + m + ((m - n) % 3 + 1) % 3 * 3

print(tot)
