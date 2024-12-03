import shutil
import sys
from time import perf_counter_ns

from aoc2024 import util
from datetime import datetime
from colorama import init as colorama_init, Fore
from importlib import import_module
from pathlib import Path

colorama_init(autoreset=True)


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return f'%.{"0" if magnitude <= 1 else "1"}f %s' % (num, ['nanoseconds', 'microseconds', 'milliseconds', 'seconds'][magnitude])


if __name__ == '__main__':
    today = datetime.today()

    if len(sys.argv) == 1:
        if today.year != 2024 or today.month != 12:
            print(f'{Fore.RED}Error: Can\'t run without specific day outside of competition time.')
            exit(1)
        target_day = str(today.day)
    else:
        target_day = sys.argv[1]

    if int(target_day) > today.day and today.year == 2024:
        print(f'{Fore.RED}Error: Can\'t run future day')
        exit(1)
    target_day = target_day.zfill(2)
    if not Path(f'aoc2024/day{target_day}.py').is_file():
        # create from template
        print(f'{Fore.YELLOW}Generating day {target_day}...')
        shutil.copyfile('template/day.py', f'aoc2024/day{target_day}.py')
    print(f'{Fore.YELLOW}Running day {target_day} ({Fore.CYAN}https://adventofcode.com/2024/day/{int(target_day)}{Fore.YELLOW})...')
    data = util.get_data(int(target_day))
    day_module = import_module(f'aoc2024.day{target_day}')
    start_time = perf_counter_ns()
    r1, r2 = day_module.process(data)
    elapsed = perf_counter_ns() - start_time
    print(f'Part 1: {Fore.CYAN}{r1}')
    print(f'Part 2: {Fore.CYAN}{r2}')
    print(f'Elapsed: {Fore.GREEN}{human_format(elapsed)}')


