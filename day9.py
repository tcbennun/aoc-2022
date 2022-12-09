import numpy as np

def lmao(n):
    r = np.tile(np.r_[0, 0], (n, 1))
    v = [(0, 0)]
    for l in open("day9.txt"):
        for _ in range(int(l[2:])):
            r[0] += {
                "L": (-1, 0),
                "R": (1, 0),
                "U": (0, 1),
                "D": (0, -1),
            }[l[0]]
            for i in range(n - 1):
                t = r[i + 1]
                d = r[i] - t
                if np.max(np.abs(d)) > 1:
                    t += np.sign(d)
            v.append((r[-1, 0], r[-1, 1]))
    print(len(set(v)))

lmao(2)
lmao(10)
