def has_gap(blocks):
    bids = [i for i, x in enumerate(blocks) if not isinstance(x, int)]
    return not all(bids[i] == bids[i-1] + 1 for i in range(1, len(bids)))


def calc_hash(blocks):
    idx = 0
    total = 0
    for block in blocks:
        if isinstance(block, int):
            idx += block
        else:
            for _ in range(block[1]):
                total += block[0] * idx
                idx += 1
    return total


def str_blocks(blocks):
    return ''.join('.' * b if isinstance(b, int) else str(b[0]) * b[1] for b in blocks)


def p1(blocks) -> int:
    while has_gap(blocks):
        gids = [i for i, x in enumerate(blocks) if isinstance(x, int)]
        bids = [i for i, x in enumerate(blocks) if not isinstance(x, int)]
        gap = blocks[gids[0]]
        if blocks[bids[-1]][1] <= gap:
            # reduce gap size
            blocks[gids[0]] -= blocks[bids[-1]][1]
            # remove old
            b = blocks[bids[-1]]
            blocks.pop(bids[-1])
            # insert block
            blocks.insert(gids[0], b)
        else:
            # fill gap and reduce
            rem = blocks[bids[-1]][1] - blocks[gids[0]]
            blocks[gids[0]] = (blocks[bids[-1]][0], blocks[gids[0]])
            blocks[bids[-1]] = (blocks[bids[-1]][0], rem)
    return calc_hash(blocks)


def p2(blocks) -> int:
    to_move = [x[0] for i, x in enumerate(blocks) if not isinstance(x, int)]
    for m in reversed(to_move):
        gids = [i for i, x in enumerate(blocks) if isinstance(x, int) and x > 0]
        bid = next(i for i, x in enumerate(blocks) if not isinstance(x, int) and x[0] == m)
        for gid in gids:
            if gid >= bid:
                break
            if blocks[gid] >= blocks[bid][1]:
                # reduce gap size
                blocks[gid] -= blocks[bid][1]
                # remove old
                b = blocks[bid]
                blocks[bid] = b[1]
                # insert block
                blocks.insert(gid, b)
                break
    return calc_hash(blocks)


def process(data):
    data = list(map(int, data[0]))
    fl, sl, *remain = data
    blocks = []
    fid = 0
    # input processing
    while remain:
        blocks.append((fid, fl))
        if sl > 0:
            blocks.append(sl)
        fid += 1
        if len(remain) > 2:
            fl, sl, *remain = remain
        else:
            blocks.append((fid, remain[0]))
            remain = None

    return p1(blocks.copy()), p2(blocks.copy())
