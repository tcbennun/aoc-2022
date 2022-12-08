import numpy as np

z = np.zeros
a = np.maximum.accumulate

d = np.array([[int(n) for n in l.strip()] for l in open("day8.txt")])
h, w = d.shape

D = np.c_[z((h + 2, 1)), np.r_[z((1, w)), d, z((1, w))], z((h + 2, 1))]
print(np.sum(~(
    ((D[1:    ] - a(D,          0)[:-1      ])[1:-2, 2:-2] <= 0) &
    ((D[:,  1:] - a(D,          1)[:,    :-1])[2:-2, 1:-2] <= 0) &
    ((D[:-1   ] - a(D[::-1],    0)[-2::-1   ])[2:-1, 2:-2] <= 0) &
    ((D[:, :-1] - a(D[:, ::-1], 1)[:, -2::-1])[2:-2, 2:-1] <= 0)
)) + 2 * (h + w) - 4)

print(max([np.product([np.argmax(np.r_[s, 9] >= d[y, x]) + 1 for s in (
    d[y, x + 1:-1], d[y, x - 1:0:-1], d[y + 1:-1, x], d[y - 1:0:-1, x]
)]) for y in range(1, h - 1) for x in range(1, w - 1)]))
