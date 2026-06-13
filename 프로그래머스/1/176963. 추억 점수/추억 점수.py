def solution(name, yearning, photo):
    name_weight = {names : year for names, year in zip(name, yearning)}
    result = []
    for i in range(len(photo)):
        cnt = 0
        for j in photo[i]:
            if j in name: 
                cnt += name_weight[j]
        result.append(cnt)
    return result

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name,yearning,photo))



