import re

def do_it(f, part2):
    lines = [line for line in open(f)]
    N = (len(lines[0])) // 4
    ss = [[] for _ in range(N)]

    for i, line in enumerate(lines):
        if line.startswith(" 1"):
            break
        for i in range(N):
            c = line[4*i + 1]
            if c != " ":
                ss[i].append(c)

    for line in lines[i + 2:]:
        n, a, b = (int(x) for x in re.match(r"move (\d+) from (\d+) to (\d+)", line).groups())
        a, b = a - 1, b - 1
        ss[b] = ss[a][:n][::part2 * 2 - 1] + ss[b] # :)
        ss[a] = ss[a][n:]

    print("".join([s[0] for s in ss]))

do_it("day5.txt", False)
do_it("day5.txt", True)
