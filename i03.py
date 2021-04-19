from itertools import combinations
import re

# 불량사용자 문제
# *로 일부가 가려진 id 리스트를 주었을 때
# 리스트와 매칭 가능한 id 조합의 갯수 구하기
# 불량사용자 리스트와 같은 크기의 id조합을 구한 후 매칭검사
def solution(user_id, banned_id):
    answer = 0
    cands = list(combinations(user_id, len(banned_id)))
    for cand in cands:
        answer += match(cand, banned_id, len(banned_id), 0)
    return answer
    
# 완전탐색
def match(cand, banned_id, l, d):
    # 불량 사용자의 수만큼 매칭완료시
    if(d==l):
        return 1
    
    res = 0
    banned = banned_id[-1]  # 현 단계에서 제재할 아이디
    passing = banned_id[:-1]    # 그 외의 제재 리스트
    for user in cand:
        # 매칭되는 유저id를 찾았을 경우
        # 해당 유저를 리스트에서 제거하고 다음단계로
        if(len(user)==len(banned) and re.match(banned.replace('*', '.'), user)):
            res += match([item for item in cand if(item!=user)], passing, l, d+1)
    
    return min(1, res)
        
        
    