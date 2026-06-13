import math
from itertools import permutations

def solution(picks, minerals):
    # picks [다이아, 철, 돌]
    count_size = math.ceil(len(minerals) / 5)
    count_mat = [[0] * count_size, [0] * count_size, [0] * count_size] # 다이아 철 돌
    for idx, mineral in enumerate(minerals) :
        if mineral == "stone":
            count_mat[0][idx // 5] += 1
            count_mat[1][idx // 5] += 1
            count_mat[2][idx // 5] += 1
        elif mineral == "iron":
            count_mat[0][idx // 5] += 1
            count_mat[1][idx // 5] += 1
            count_mat[2][idx // 5] += 5
        elif mineral == "diamond":
            count_mat[0][idx // 5] += 1
            count_mat[1][idx // 5] += 5
            count_mat[2][idx // 5] += 25
    my_picks = [0, 0, 0]
    my_have = []
    for i in range(count_size):
        if picks[0] > 0:
            my_have.append(0)
            picks[0] -= 1
        elif picks[1] > 0:
            my_have.append(1)
            picks[1] -= 1
        elif picks[2] > 0:
            my_have.append(2)
            picks[2] -= 1
        else:
            break
    
    ans = float('inf')
    for comb in permutations(my_have):
        s = 0
        for idx, i in enumerate(comb):
            s += count_mat[i][idx]
        ans = min(ans, s)
        
    return ans