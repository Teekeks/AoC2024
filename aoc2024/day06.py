walk_dir_lookup = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1),
}
turn_lookup = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}


def is_loop(obstacles, start_pos, start_dir) -> bool:
    px, py = start_pos
    visited_dirs = set()
    walk_dir = start_dir
    while True:
        # reached finish
        if px < 0 or py < 0 or px >= len(obstacles) or py >= len(obstacles[px]):
            return False
        if obstacles[px][py]:
            # turn 90°
            px, py = px - walk_dir[0], py - walk_dir[1]
            walk_dir = turn_lookup[walk_dir]
        elif (px, py, walk_dir[0], walk_dir[1]) in visited_dirs:
            return True
        else:
            visited_dirs.add((px, py, walk_dir[0], walk_dir[1]))
            px, py = px + walk_dir[0], py + walk_dir[1]


def process(data):
    start = None
    obstacles = []
    visited = set()
    start_dir = None
    for x in range(len(data)):
        obstacles.append([])
        for y in range(len(data[x]) - 1):
            obstacles[x].append(data[x][y] == '#')
            if data[x][y] in walk_dir_lookup:
                start = (x, y)
                start_dir = walk_dir_lookup[data[x][y]]
    walk_dir = start_dir
    position = start
    while True:
        visited.add(position)
        mov = (position[0] + walk_dir[0], position[1] + walk_dir[1])
        # reached finish
        if mov[0] < 0 or mov[1] < 0 or mov[0] >= len(obstacles) or mov[1] >= len(obstacles[mov[0]]):
            break
        if obstacles[mov[0]][mov[1]]:
            # turn 90°
            walk_dir = turn_lookup[walk_dir]
            mov = (position[0] + walk_dir[0], position[1] + walk_dir[1])
        position = mov
    r1 = len(visited)
    possible = []
    for x in range(len(obstacles)):
        for y in range(len(obstacles[x])):
            if not obstacles[x][y] and (x, y) != start:
                obstacles[x][y] = True
                if is_loop(obstacles, start, start_dir):
                    possible.append((x, y))
                obstacles[x][y] = False

    r2 = len(possible)
    return r1, r2
