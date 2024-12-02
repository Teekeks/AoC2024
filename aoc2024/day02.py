def is_safe(levels):
    start = levels[0]
    for level in levels[1:]:
        if abs(start - level) < 1 or abs(start - level) > 3:
            break
        start = level
    else:
        if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
            return True
    return False


def process(data):
    r1, r2 = 0, 0
    for report in data:
        levels = list(map(int, report.split()))
        if is_safe(levels):
            r1 += 1
        else:
            # try removing a single value and recheck
            for i in range(len(levels)):
                t = levels.copy()
                t.pop(i)
                if is_safe(t):
                    r2 += 1
                    break
    r2 += r1
    return r1, r2
