from aoc2024.util import Grid


def walls_for_cell(c, cells):
    w = set()
    for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if (c[0] + x, c[1] + y) not in cells:
            w.add((c[0], c[1], c[0] + x / 2 if x != 0 else c[0], c[1] + y / 2 if y != 0 else c[1]))
    return w


def process(data):
    r1, r2 = 0, 0
    grid = Grid.from_string_list(data, str)
    for cells in grid.regions():
        p1 = 0
        all_walls = set()
        for c in cells:
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (c[0] + dx, c[1] + dy) not in cells:
                    p1 += 1
            all_walls |= walls_for_cell(c, cells)
        # get first wall
        w = next(iter(all_walls))
        seen = {w}
        p2 = 0
        while w:
            p2 += 1
            # walk current wall in both directions
            for a in (1, -1):
                x = a if isinstance(w[2], int) else 0
                y = 0 if x != 0 else a
                while (w[0] + x, w[1] + y, w[2] + x, w[3] + y) in all_walls:
                    seen.add((w[0] + x, w[1] + y, w[2] + x, w[3] + y))
                    x += a if isinstance(w[2], int) else 0
                    y += 0 if x != 0 else a
            # find first wall not seen yet
            try:
                w = next(b for b in all_walls if b not in seen)
                seen.add(w)
            except StopIteration:
                break
            seen.add(w)
        r2 += len(cells) * p2
        r1 += len(cells) * p1
    return r1, r2
