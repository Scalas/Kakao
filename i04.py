def solution(stones, k):
    answer = 0
    l = 0
    r = max(stones)
    while(l <= r):
        m = (l+r)//2
        if(check(stones, m, k)):
            answer = m
            l = m+1
        else:
            r = m-1
            
    return answer


def check(stones, m, k):
    count = 0
    for stone in stones:
        if(stone < m):
            count += 1
        else:
            count = 0
        if(count==k):
            return False
    return True