import numpy as np

grid = np.array([[ord(n) for n in l.strip()] for l in open("day12.txt")])
def grid_at(pos):
    return grid[pos[0], pos[1]]
def grid_at_set(pos, val):
    grid[pos[0], pos[1]] = val

start = np.argwhere(grid == ord("S"))[0]
grid_at_set(start, ord("a"))

dest = np.argwhere(grid == ord("E"))[0]
grid_at_set(dest, ord("z"))

dist = np.full_like(grid, np.inf, dtype=float)
visited = np.full_like(grid, False, dtype=bool)

dist[dest[0], dest[1]] = 0

directions = [np.array((r, c)) for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1))]

while not np.all(visited):
    v = np.where(~visited)
    v_r, v_c = v
    lmao = np.c_[v_r, v_c, dist[v]]
    lmao = lmao[lmao[:, 2].argsort()]
    r, c, _ = lmao[0]
    r, c = int(r), int(c)
    u = np.array([r, c])
    visited[r, c] = True
    for dir in directions:
        v = u + dir
        if not (np.all(v >= 0) and v[0] < grid.shape[0] and v[1] < grid.shape[1]):
            continue
        r1, c1 = v
        if visited[r1, c1]:
            continue
        d = 1.0 if grid[r, c] - grid[r1, c1] <= 1 else np.inf
        alt = dist[r, c] + d
        if alt < dist[r1, c1]:
            dist[r1, c1] = alt

d_r, d_c = start
print(int(dist[d_r, d_c]))
print(int(np.sort(dist[grid == ord("a")])[0]))
