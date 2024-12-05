def intersection(a, b):
    return [v for v in a if v in b]


def is_ordered(l, rules) -> bool:
    visited = []
    for entry in l:
        if len(intersection(visited, rules.get(entry, []))) > 0:
            return False
        visited.append(entry)
    else:
        return True


def process(data):
    r1, r2 = 0, 0
    rules = {}
    for line in data:
        if '|' in line:
            p1, p2 = map(int, line.split('|'))
            if p1 in rules:
                rules[p1].append(p2)
            else:
                rules[p1] = [p2]
        elif ',' in line:
            page = list(map(int, line.split(',')))
            if is_ordered(page, rules):
                r1 += page[len(page) // 2]
            else:
                # is unordered -> find ordered
                remaining = set(page)
                new_page = []
                while remaining:
                    for n in remaining:
                        if len(intersection(rules.get(n, []), remaining)) == (len(remaining) - 1):
                            new_page.append(n)
                            remaining.remove(n)
                            break
                r2 += new_page[len(new_page) // 2]
    return r1, r2
