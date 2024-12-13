import re
from aoc2024.util import range_2d
import z3

RE_PATTERN = re.compile(r'\d+')


def opt(ax, ay, bx, by, px, py):
    a = z3.Int(ax)
    b = z3.Int(ay)
    o = z3.Optimize()
    o.add(a >= 0)
    o.add(b >= 0)
    o.add(a * ax + b * bx == px)
    o.add(a * ay + b * by == py)
    obj = o.minimize(3 * a + b)
    if o.check() == z3.sat:
        return obj.value().as_long()
    return 0


def process(data):
    r1, r2 = 0, 0
    for claw in '\n'.join(data).split('\n\n'):
        ax, ay, bx, by, px, py = map(int, RE_PATTERN.findall(claw))
        options = [3 * a + b for a, b in range_2d(101, 101) if (a * ax + b * bx, a * ay + b * by) == (px, py)]
        if len(options) > 0:
            r1 += min(options)
        r2 += opt(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)
    return r1, r2
