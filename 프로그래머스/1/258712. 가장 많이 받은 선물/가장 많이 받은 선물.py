def solution(friends, gifts):
    gift_index = {}
    send_friend_count = {}
    ans = {}
    for friend in friends:
        gift_index[friend] = 0
        ans[friend] = 0
        send_friend_count[friend] = {f : 0 for f in friends if f != friend}
        
    for gift in gifts:
        sender, receiver = gift.split()
        gift_index[sender] += 1
        gift_index[receiver] -= 1
        send_friend_count[sender][receiver] += 1
        send_friend_count[receiver][sender] -= 1
    
            
    print(gift_index)
    for sender in send_friend_count:
        for receiver, count in send_friend_count[sender].items():
            print(sender, receiver, count)
            if count > 0:
                ans[sender] += 1
            elif count == 0:
                if gift_index[sender] > gift_index[receiver]:
                    ans[sender] += 1
    
    return max(ans.values())
        
    

            
        