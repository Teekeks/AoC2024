from collections import deque

W, H = 0, 0


def find_tops(data, start, is_p2=False) -> int:
    visited = set()
    s = 0
    queue = deque([start])
    while queue:
        p = queue.pop()
        if not is_p2:
            visited.add(p)
        if data[p[0]][p[1]] == 9:
            s += 1
        for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= p[0] + x < W and 0 <= p[1] + y < H and (p[0] + x, p[1] + y) not in visited and data[p[0] + x][p[1] + y] - 1 == data[p[0]][p[1]]:
                queue.append((p[0] + x, p[1] + y))
    return s


def process(data):
    r1, r2 = 0, 0
    data = [list(map(int, [x for x in d])) for d in data]
    global W, H
    H = len(data)
    W = len(data[0])
    for trailhead in [(x, y) for y in range(H) for x in range(W) if data[x][y] == 0]:
        r1 += find_tops(data, trailhead)
        r2 += find_tops(data, trailhead, is_p2=True)
    return r1, r2
