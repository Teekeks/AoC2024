from aoc2024.util import get_data
from pprint import pprint


def process(data):
    l1 = list()
    l2 = list()
    tally = 0
    for entry in data:
        e1, e2 = entry.split('   ')
        l1.append(int(e1))
        l2.append(int(e2))
    for e1, e2 in zip(sorted(l1), sorted(l2)):
        tally += abs(e1 - e2)
    r1 = tally
    tally = 0
    lookup = {}
    for e in l2:
        if e not in lookup:
            lookup[e] = 1
        else:
            lookup[e] += 1
    for e in l1:
        tally += e * lookup.get(e, 0)
    return r1, tally
