import heapq

def solution(n, k, enemy):
    heap = []
    cnt = 0
    
    for e in enemy:
        n -= e
        heapq.heappush(heap, -e)
        
        while n < 0 and heap: 
            if k <= 0:
                return cnt
            max_e = heapq.heappop(heap)
            n -= max_e
            k -= 1


        cnt += 1

    return cnt