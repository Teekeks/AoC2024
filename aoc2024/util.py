import os.path

import requests
import json


def get_data(day: int):
    if os.path.isfile(f'data/{day}.txt'):
        with open(f'data/{day}.txt') as f:
            return [s for s in f.readlines()]
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
        return [s for s in f.readlines()]
