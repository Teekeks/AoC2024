import itertools
import operator as op
from functools import partial


def solve(funcs, result, ns):
    a, b, *rest = ns
    for fs in itertools.product(funcs, repeat=len(ns) - 1):
        x = fs[0](a, b)
        for i, n in enumerate(rest, 1):
            x = fs[i](x, n)
        if x == result:
            return result
    return 0


def process(data):
    results = []
    nums = []
    for line in data:
        val, raw_vals = line.split(':')
        results.append(int(val))
        nums.append(list(map(lambda x: int(x.strip()), raw_vals.split())))
    r1 = sum(map(partial(solve, [op.add, op.mul]), results, nums))
    r2 = sum(map(partial(solve, [op.add, op.mul, lambda a, b: int(str(a) + str(b))]), results, nums))
    return r1, r2
