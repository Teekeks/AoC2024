W, H = 0, 0
obstacles = []
start = set()


def is_loop(ax, ay) -> bool:
    px, py = start
    dx, dy = -1, 0
    visited_dirs = set()
    while True:
        # reached finish
        if px < 0 or py < 0 or px >= H or py >= W:
            return False
        if obstacles[px][py] or (ax == px and ay == py):
            # step back & turn 90°
            px, py = px - dx, py - dy
            dx, dy = dy, -dx
        elif (px, py, dx, dy) in visited_dirs:
            return True
        else:
            visited_dirs.add((px, py, dx, dy))
            px, py = px + dx, py + dy


def count_steps() -> int:
    px, py = start
    visited = set()
    dx, dy = -1, 0
    while True:
        # reached finish
        if px < 0 or py < 0 or px >= H or py >= W:
            return len(visited)
        if obstacles[px][py]:
            # step back & turn 90°
            px, py = px - dx, py - dy
            dx, dy = dy, -dx
        else:
            visited.add((px, py))
            px, py = px + dx, py + dy


def process(data):
    global W, H, obstacles, start
    obstacles = [[data[x][y] == '#' for y in range(len(data[0]) - 1)] for x in range(len(data))]
    H = len(obstacles)
    W = len(obstacles[0])
    start = next((x, y) for x in range(H) for y in range(W) if data[x][y] == '^')
    r1 = count_steps()
    r2 = sum(1 if is_loop(x, y) else 0 for x in range(H) for y in range(W) if not obstacles[x][y] and (x, y) != start)
    return r1, r2
