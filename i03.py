from itertools import combinations
import re

def solution(user_id, banned_id):
    answer = 0
    cands = list(combinations(user_id, len(banned_id)))
    for cand in cands:
        answer += match(cand, banned_id, len(banned_id), 0)
    return answer
    
def match(cand, banned_id, l, d):
    if(d==l):
        return 1
    
    res = 0
    banned = banned_id[-1]
    passing = banned_id[:-1]
    for user in cand:
        if(len(user)==len(banned) and re.match(banned.replace('*', '.'), user)):
            res += match([item for item in cand if(item!=user)], passing, l, d+1)
    
    return min(1, res)
        
        
    