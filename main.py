from aoc2024 import util, day01, day02
from datetime import datetime
import humanize

lookup = {
    1: day01,
    2: day02,
}


def default():
    print('current day not there yet')


# execute current day
if __name__ == '__main__':
    current_day = datetime.today().day
    if current_day not in lookup:
        default()
    else:
        data = util.get_data(current_day)
        start = datetime.now()
        r1, r2 = lookup[current_day].process(data)
        elapsed = datetime.now() - start
        print(f'Part 1: {r1}\n'
              f'Part 2: {r2}\n'
              f'Elapsed: {humanize.precisedelta(elapsed, minimum_unit='microseconds')}')

