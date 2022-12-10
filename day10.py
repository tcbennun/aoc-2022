d = []
x_next = 1
for l in open("day10.txt"):
    if l[0] == "a":
        d += [x_next, x_next]
        x_next += int(l[5:])
    else:
        d.append(x_next)

print(sum(c * d[c - 1] for c in (20, 60, 100, 140, 180, 220)))

print()
for y in range(6):
    for x in range(40):
        print("#" if abs(x - d[40 * y + x]) <= 1 else " ", end="")
    print()
