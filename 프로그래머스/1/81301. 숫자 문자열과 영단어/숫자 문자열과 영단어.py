def solution(s):
    num = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    word = ""
    ans = ""
    for i in s:
        if 'a' <= i <= 'z':
            word += i
        else: ans += i
        if word in num.keys():
            ans += str(num[word])
            word = ""
    return int(ans)
            