from functools import cache


def process(data):
    @cache
    def sim(val, nr):
        if nr == 0:
            return 1
        s = str(val)
        if val == 0:
            return sim(1, nr - 1)
        elif len(s) % 2 == 0:
            return sim(int(s[:len(s) // 2:]), nr - 1) + sim(int(s[len(s) // 2:]), nr - 1)
        else:
            return sim(val * 2024, nr - 1)

    data = list(map(int, data[0].split()))
    return sum(sim(i, 25) for i in data), sum(sim(i, 75) for i in data)
