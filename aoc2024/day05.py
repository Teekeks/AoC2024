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
    before = {}
    pages = []
    for line in data:
        if '|' in line:
            p1, p2 = map(int, line.split('|'))
            if p1 in before:
                before[p1].append(p2)
            else:
                before[p1] = [p2]
        elif ',' in line:
            pages.append(list(map(int, line.split(','))))
    ordered_pages = []
    unordered_pages = []
    for page in pages:
        if is_ordered(page, before):
            ordered_pages.append(page)
        else:
            unordered_pages.append(page)
    r1 = sum([o[len(o) // 2] for o in ordered_pages])
    new_ordered = []
    for page in unordered_pages:
        remaining = set(page)
        new_page = []
        while remaining:
            for n in remaining:
                if len(intersection(before.get(n, []), remaining)) == (len(remaining) - 1):
                    new_page.append(n)
                    remaining.remove(n)
                    break
        new_ordered.append(new_page)
    r2 = sum([o[len(o) // 2] for o in new_ordered])
    return r1, r2
