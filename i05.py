# 징검다리 문제
# 징검다리마다 밟을 수 있는 횟수가 정해져있고
# 최대 k개의 다리를 건너뛸수 잇을 때
# 최대 몇 명이 다리를 건널 수 있는가

# 결국 k크기의 연속구간의 최댓값 중 최솟값이 답이된다
# 슬라이딩 윈도우를 통해 구할경우 복잡도가 O(N^2)으로 시간초과
# 최댓값이 갱신되는 조건을 체크하여 시간을 줄일 수 있지만
# 최대값이 자주 갱신되고 원하는 연속구간이 시작위치에서 멀어지면
# 시간초과가 발생

# 이분탐색이 그나마 떠올리기 쉽고 O(NlogM) 복잡도로 해결가능
# 0과 징검다리 최댓값 사이에서 이분탐색을 통해 최댓값을 탐색 
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