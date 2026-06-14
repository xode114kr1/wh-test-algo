# 중위 순회

def solution(numbers):
    def add_size(b_mum):
        n = len(b_mum)
        size = 1
        while size <= n:
            size *= 2
        gap = size - n - 1
        return "0" * gap + b_mum
    
    def can(b_num, isZero):
        n = len(b_num)
        mid = n // 2
        if b_num[mid] == "1" and isZero:
            return False
        if n == 1:
            return True
        if b_num[mid] == "0":        
            return can(b_num[:mid], True) and can(b_num[mid + 1:], True)
        else:
            return can(b_num[:mid], False) and can(b_num[mid + 1:], False)
    
    ans = []
    for num in numbers:
        bi = bin(num)[2:]
        bi = add_size(bi)
        
        if can(bi, False):
            ans.append(1)
        else:
            ans.append(0)
    return ans
        