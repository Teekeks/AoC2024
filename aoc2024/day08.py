from itertools import combinations
from collections import defaultdict


def process(data):
    w, h = len(data), len(data[0])
    antenas = defaultdict(set)
    p1 = set()
    p2 = set()
    for x, line in enumerate(data):
        for y, p in enumerate(line):
            if p == '.':
                continue
            antenas[p].add((x, y))

    def in_bounds(_x, _y):
        return 0 <= _x < w and 0 <= _y < h

    for nodes in antenas.values():
        for (ax, ay), (bx, by) in combinations(nodes, 2):
            p2.add((ax, ay))
            p2.add((bx, by))
            dx, dy = bx - ax, by - ay
            nx, ny = ax - dx, ay - dy
            if in_bounds(nx, ny):
                p1.add((nx, ny))
            while in_bounds(nx, ny):
                p2.add((nx, ny))
                nx -= dx
                ny -= dy
            mx, my = bx + dx, by + dy
            if in_bounds(mx, my):
                p1.add((mx, my))
            while in_bounds(mx, my):
                p2.add((mx, my))
                mx += dx
                my += dy
    return len(p1), len(p2)
