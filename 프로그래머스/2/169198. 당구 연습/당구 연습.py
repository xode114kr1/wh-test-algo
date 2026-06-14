def solution(m, n, startX, startY, balls):
    def count_time(sx, sy, ex, ey):
        cand = []
        if not (sy == ey and sx > ex):
            cand.append((sx - (-ex)) ** 2 + (sy - ey) ** 2)

        if not (sy == ey and sx < ex):
            cand.append((sx - (2 * m - ex)) ** 2 + (sy - ey) ** 2)

        if not (sx == ex and sy > ey):
            cand.append((sx - ex) ** 2 + (sy - (-ey)) ** 2)

        if not (sx == ex and sy < ey):
            cand.append((sx - ex) ** 2 + (sy - (2 * n - ey)) ** 2)

        return min(cand)
    answer = []
    for x, y in balls:
        answer.append(count_time(startX, startY, x, y))

    return answer