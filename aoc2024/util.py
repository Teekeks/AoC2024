import os.path
import typing
from collections import deque

import requests
import json


def get_data(day: int):
    if os.path.isfile(f'data/{day}.txt'):
        with open(f'data/{day}.txt') as f:
            return [s[:-1] for s in f.readlines()]
    with open('config.json', 'r') as f:
        cfg = json.load(f)
    cookies = {
        'session': cfg['session']
    }
    headers = {
        'User-Agent': cfg['user-agent']
    }
    req = requests.get(f'https://adventofcode.com/2024/day/{day}/input', cookies=cookies, headers=headers)
    with open(f'data/{day}.txt', 'w') as f:
        for line in req.text.splitlines():
            f.write(f'{line}\n')
    with open(f'data/{day}.txt') as f:
        return [s[:-1] for s in f.readlines()]


def range_2d(x, y) -> set:
    for _x in range(x):
        for _y in range(y):
            yield _x, _y


T = typing.TypeVar('T')
U = typing.TypeVar('U')


class Grid(typing.Generic[T]):

    data: list[list[T]]

    def __init__(self, data: list[list[T]]):
        self.data = data

    @classmethod
    def from_string(cls, raw: str, t: typing.Callable[[str], U]) -> 'Grid[U]':
        return Grid(list(map(lambda i: list(map(t, i)), raw.splitlines())))

    @classmethod
    def from_string_list(cls, raw: list[str], t: typing.Callable[[str], U]) -> 'Grid[U]':
        return Grid(list(map(lambda i: list(map(t, i)), raw)))

    @property
    def width(self) -> int:
        return len(self.data[0])

    @property
    def height(self) -> int:
        return len(self.data)

    def region(self,
               start: tuple[int, int],
               is_in_region: typing.Callable[[tuple[int, int], T, tuple[int, int], T], bool] =
               lambda from_pos, from_cell, to_pos, to_cell: (from_cell == to_cell)) -> set[tuple[int, int]]:
        """returns a region of points"""
        result = set()
        q = deque([start])
        while q:
            cell = q.popleft()
            if cell in result:
                continue
            result.add(cell)
            x, y = cell
            for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                    if is_in_region(cell, self.data[x][y], (x + dx, y + dy), self.data[x + dx][y + dy]):
                        q.append((x + dx, y + dy))
        return result

    def regions(self,
                is_in_region: typing.Callable[[tuple[int, int], T, tuple[int, int], T], bool] =
                lambda from_pos, from_cell, to_pos, to_cell: (from_cell == to_cell)) -> list[set[tuple[int, int]]]:
        """returns a list of regions of points"""
        result = []
        seen = set()
        for cell in range_2d(self.width, self.height):
            if cell in seen:
                continue
            cells = self.region(cell, is_in_region)
            result.append(cells)
            seen = seen.union(cells)
        return result

    @typing.overload
    def __getitem__(self, index: tuple[int, int]) -> T: ...

    @typing.overload
    def __getitem__(self, index: int) -> list[T]: ...

    def __getitem__(self, index):
        if isinstance(index, tuple):
            x, y = index
            return self.data[x][y]
        return self.data[index]
