def solution(n):
    for i in range(1, n):
        if n % i == 1: break
    return i