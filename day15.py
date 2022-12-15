import re
import numpy as np

def pt1():
    incl = set()
    excl = []
    for l in open("day15.txt"):
        xs, ys, xb, yb = (int(n) for n in re.match(r"Sensor at x=(-?\d+), y=(-?\d+):.*x=(-?\d+), y=(-?\d+)$", l).groups())
        md = abs(xs - xb) + abs(ys - yb)
        r = 2000000
        d = md - abs(ys - r)
        if d >= 0:
            incl |= set(range(xs - d, xs + d + 1))
        if yb == r:
            excl.append(xb)

    result = incl.difference(set(excl))
    print(len(result))

class Scan:
    def __init__(self, xs, ys, xb, yb):
        self.xs, self.ys, self.xb, self.yb = xs, ys, xb, yb
        self.p_s, self.p_b = np.array([xs, ys]), np.array([xb, yb])

        self.dist = abs(xs - xb) + abs(ys - yb)

        self.corners = [
            self.p_s + np.array([0, -self.dist]),
            self.p_s + np.array([self.dist, 0]),
            self.p_s + np.array([0, self.dist]),
            self.p_s + np.array([-self.dist, 0]),
        ]

def almost_adjacent(lhs: Scan, rhs: Scan):
    c, d = lhs.corners, rhs.corners
    z = zip(
        ((c[0], c[1]), (c[1], c[2]), (c[2], c[3]), (c[3], c[0])),
        ((d[2], d[3]), (d[3], d[0]), (d[0], d[1]), (d[1], d[2])),
        (np.array(o) for o in ((1, -1), (1, 1), (-1, 1), (-1, -1))),
        (np.array(o) for o in ((1,  0), (0, 1), (-1, 0), ( 0, -1))),
    )
    for (r1, r2), (q1, q2), o, p in z:
        a1 = along_line(r1 + o, r2 + o, q1)
        a2 = along_line(r1 + o, r2 + o, q2)
        if None not in (a1, a2) and not (a1 <= 0 and a2 <= 0) and not (a1 >= 1.0 and a2 >= 1.0):
            return r1 + p, r2 + p
    return None

def along_line(r1, r2, q1):
    l = (q1 - r1) / (r2 - r1)
    if np.all(l == l[0]):
        return l[0]
    else:
        return None

def intersection(r0, r1, p0, p1):
    r0x, r0y = r0
    p0x, p0y = p0
    r = r1 - r0
    rx, ry = r
    px, py = p1 - p0
    return r0 + (px * (p0y - r0y) - py * (p0x - r0x)) / (px * ry - py * rx) * r

def pt2():
    # note: absolutely does not work for the example data

    fname, search_size = "day15.txt", 4000000

    scans = [Scan(*(int(n) for n in re.match(r"Sensor at x=(-?\d+), y=(-?\d+):.*x=(-?\d+), y=(-?\d+)$", l).groups())) for l in open(fname)]

    h = []
    for i in range(len(scans) - 1):
        for j in range(i + 1, len(scans)):
            adj = almost_adjacent(scans[i], scans[j])
            if adj != None:
                h.append(adj)

    isct = intersection(
        h[0][0],
        h[0][1],
        h[1][0],
        h[1][1],
    )

    print(int(isct[0] * search_size + isct[1]))

pt1()
pt2()
