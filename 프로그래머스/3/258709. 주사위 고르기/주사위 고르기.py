from collections import defaultdict
from itertools import combinations


def solution(dice):
    n = len(dice)
    half = n // 2

    def sum_dice(idxs):
        dist = {0 : 1}
        for i in idxs:
            nd = defaultdict(int)
            faces = dice[i]
            for s, c in dist.items():
                for f in faces:
                    nd[s + f] += c
            dist = nd
        return dist


    best_win = -1
    best_pick = None
    dice_idx = [i for i in range(n)]

    for com_idx in combinations(dice_idx, half):
        set_a = list(com_idx)
        set_b = [idx for idx in dice_idx if idx not in set_a]

        dist_a = sum_dice(set_a)
        dist_b = sum_dice(set_b)

        b_items = sorted(dist_b.items())
        b_sums = [s for s, _ in b_items]
        b_pref = []
        acc = 0
        for _, v in b_items:
            acc += v
            b_pref.append(acc)
        # print(b_pref)

        def count_b_less(x):
            lo, hi = 0, len(b_pref)
            while lo < hi:
                mid = (lo + hi) // 2
                if b_sums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return b_pref[lo - 1] if lo > 0 else 0

        win = 0
        for a_sum, a_cnt in dist_a.items():
            win += a_cnt * count_b_less(a_sum)

        if win > best_win:
            best_win = win
            best_pick = set_a

    return [i + 1 for i in best_pick]