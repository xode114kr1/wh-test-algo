from collections import defaultdict

def solution(points, routes):
    len_routes = len(routes)
    dic = defaultdict(int) # (x, y, time) : cnt

    def save_move(start, end, time):
        cur_x, cur_y = start
        point_x, point_y = end
        while 1:
            move_x = (point_x - cur_x)
            move_y = (point_y - cur_y)
            if move_x != 0:
                # x좌표 차이가 있으면
                cur_x += move_x  // abs(point_x - cur_x)
            elif move_y != 0:
                # y좌표 차이가 있으면
                cur_y += move_y // abs(point_y - cur_y)
            else:
                # 도착했으면
                return time
            time += 1
            dic[(cur_x, cur_y, time)] += 1



    for route in routes:
        dic[points[route[0] - 1][0], points[route[0] - 1][1], 0] += 1
        time = 0
        for i in range(1, len(route)):
            start_x, start_y = points[route[i - 1] - 1]
            end_x, end_y = points[route[i] - 1]
            time = save_move((start_x, start_y), (end_x, end_y), time)

    ans = 0
    for key, val in dic.items():
        if val >= 2:
            ans += 1
    return ans