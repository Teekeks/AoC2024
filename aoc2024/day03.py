import re

RE_MUL = re.compile(r'(mul|do(?:n\'t)?)\((?:(\d{1,3}),(\d{1,3}))?\)')


def process(data):
    r1, r2 = 0, 0
    active = True
    for line in data:
        matches = RE_MUL.findall(line)
        for match in matches:
            if match[0] == 'mul':
                val = int(match[1]) * int(match[2])
                r1 += val
                if active:
                    r2 += val
            else:
                active = match[0] == 'do'
    return r1, r2
