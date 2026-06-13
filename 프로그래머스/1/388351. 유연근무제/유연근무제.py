def solution(schedules, timelogs, startday):

    def timeToNum(time):
        h, m = time // 100, time % 100
        return 60 * h + m

    n = len(schedules)
    ans = 0

    for idx in range(n):
        day = startday
        start_time = timeToNum(schedules[idx])
        isClear = True
        for i in range(7):
            if day % 7 == 6 or day % 7 == 0: # 토 / 일이면 스킵
                day += 1
                continue
            if start_time + 10 < timeToNum(timelogs[idx][i]):
                isClear = False
            day += 1
        if isClear : ans += 1
    
    return ans