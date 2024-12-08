def get(data, x, y, dirx, diry):
    ax, ay = x + dirx, y + diry
    word = 'MAS'
    for ch in word:
        if ax >= len(data) or ax < 0 or ay >= len(data[ax]) or ay < 0 or data[ax][ay] != ch:
            return 0
        ax, ay = ax + dirx, ay + diry
    return 1


def process(data):
    r1, r2 = 0, 0
    data = [list(x) for x in data]
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == 'X':
                r1 += sum(get(data, x, y, dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if not (dx == 0 and dy == 0))
            if data[x][y] == 'A':
                if (not (x < 1 or y < 1 or x >= len(data) - 1 or y >= len(data[x]) - 1) and
                        ((data[x - 1][y - 1] == 'M' and data[x + 1][y + 1] == 'S') or (data[x - 1][y - 1] == 'S' and data[x + 1][y + 1] == 'M')) and
                        ((data[x - 1][y + 1] == 'M' and data[x + 1][y - 1] == 'S') or (data[x - 1][y + 1] == 'S' and data[x + 1][y - 1] == 'M'))):
                    r2 += 1
    return r1, r2
