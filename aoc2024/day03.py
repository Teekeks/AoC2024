import re

RE_MUL = re.compile(r'(mul|do(?:n\'t)?)\((?:(\d{1,3}),(\d{1,3}))?\)')


def process(data):
    r1, r2 = 0, 0
    active = True
    for line in data:
        for match in RE_MUL.findall(line):
            if match[0] == 'mul':
                r1 += int(match[1]) * int(match[2])
                r2 += int(match[1]) * int(match[2]) if active else 0
            else:
                active = match[0] == 'do'
    return r1, r2
