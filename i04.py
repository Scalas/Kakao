import sys
sys.setrecursionlimit(100000)

# 호텔 방 배정 문제
# 빈 방을 원하는 사람에겐 그 방을
# 이미 차있는 방의 경우 원하는 방보다 큰 번호의 방중
# 가장 작은 방을 배정
def solution(k, room_number):
    answer = []
    room = {}
    # map 형태(딕셔너리)의 자료구조를 사용하여
    # 이미 배정된 방과 그 방을 원하는 손님에게 배정할 
    # 다음 방 번호를 쌍으로 저장
    for r in room_number:
        if(room.get(r)==None):
            answer.append(r)
            room[r] = next_room(room, r+1)
        else:
            empty_room = next_room(room, r)
            answer.append(empty_room)
            room[empty_room] = next_room(room, empty_room+1)
    return answer


# 재귀호출로 맵에 저장된 다음 방번호를 참조하여 빈 방을 탐색
def next_room(room, r):
    if(room.get(r)==None):
        return r
    else:
        room[r] = next_room(room, room[r])
        return room[r]