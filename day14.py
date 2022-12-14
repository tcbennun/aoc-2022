import numpy as np

rocks = []
for line in open("day14.txt"):
    coords = []
    for coords_str in line.split(" -> "):
        coords.append([int(x) for x in coords_str.split(",")])
    for i in range(1, len(coords)):
        x_0, y_0 = coords[i - 1]
        x_1, y_1 = coords[i]
        if x_0 == x_1:
            y_min, y_max = sorted([y_0, y_1])
            for y in range(y_min, y_max + 1):
                rocks.append([x_0, y])
        else:
            x_min, x_max = sorted([x_0, x_1])
            for x in range(x_min, x_max + 1):
                rocks.append([x, y_0])
rocks = np.array(rocks)

def pt1():
    x_0, x_1 = rocks[:, 0].min(), rocks[:, 0].max()
    y_0, y_1 = rocks[:, 1].min(), rocks[:, 1].max()

    x_0, x_1 = min(500, x_0), max(500, x_1)
    y_0, y_1 = min(0, y_0), max(0, y_1)

    grid = np.zeros((y_1 - y_0 + 1, x_1 - x_0 + 1))

    grid[rocks[:, 1] - y_0, rocks[:, 0] - x_0] = 1

    def chk(pos):
        x, y = pos
        return grid[y - y_0, x - x_0] == 0

    def set(pos):
        x, y = pos
        grid[y - y_0, x - x_0] = 2

    tot = 0
    while True:
        pos = [500, 0]
        stopped = False
        while not stopped and (x_0 <= pos[0] <= x_1 and y_0 <= pos[1] <= y_1):
            pos_nexts = [
                [pos[0],     pos[1] + 1],
                [pos[0] - 1, pos[1] + 1],
                [pos[0] + 1, pos[1] + 1],
            ]
            stopped = True
            for pos_next in pos_nexts:
                if chk(pos_next):
                    pos = pos_next
                    stopped = False
                    break
        if not stopped:
            break
        else:
            set(pos)
            tot += 1
    # for y in range(grid.shape[0]):
    #     for x in range(grid.shape[1]):
    #         print({0: ".", 1: "#", 2: "o"}[grid[y, x]], end="")
    #     print()
    print(tot)

def pt2():
    x_0, x_1 = rocks[:, 0].min(), rocks[:, 0].max()
    y_0, y_1 = rocks[:, 1].min(), rocks[:, 1].max()

    x_0, x_1 = min(500, x_0), max(500, x_1)
    y_0, y_1 = min(0, y_0), max(0, y_1) + 2

    grid = np.zeros((y_1 - y_0 + 1, x_1 - x_0 + 1))

    grid[rocks[:, 1] - y_0, rocks[:, 0] - x_0] = 1
    grid[-1, :] = 1

    def chk(pos):
        nonlocal x_0, y_0, grid
        x, y = pos
        c, r = x - x_0, y - y_0
        if c < 0 or c >= grid.shape[1]:
            expand = 100
            zeros = np.zeros((grid.shape[0], expand))
            grid = np.c_[zeros, grid, zeros]
            grid[-1, :] = 1
            x_0 -= expand
            c, r = x - x_0, y - y_0
        return grid[r, c] == 0

    def set(pos):
        x, y = pos
        grid[y - y_0, x - x_0] = 2

    tot = 0
    while True:
        pos = [500, 0]
        stopped = False
        while not stopped:
            pos_nexts = [
                [pos[0],     pos[1] + 1],
                [pos[0] - 1, pos[1] + 1],
                [pos[0] + 1, pos[1] + 1],
            ]
            stopped = True
            for pos_next in pos_nexts:
                if chk(pos_next):
                    pos = pos_next
                    stopped = False
                    break
        set(pos)
        tot += 1
        if pos == [500, 0]:
            break
    # for y in range(grid.shape[0]):
    #     for x in range(grid.shape[1]):
    #         print({0: ".", 1: "#", 2: "o"}[grid[y, x]], end="")
    #     print()
    print(tot)

pt1()
pt2()
