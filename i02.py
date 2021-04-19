def solution(s):
    answer = []
    # 중복제거 튜플 만들기 문제
    # 많이 반복된 수일수록 빠른순서
    numbers = list(map(int, (s.replace('{', '').replace('}', '').replace(',', ' ')).split()))
    answer = [0 for _ in range(len(set(numbers)))]

    # 반복되는 횟수-1을 인덱스로하여 저장
    for num in numbers:
        if(num not in answer):
            answer[numbers.count(num)-1] = num
    # 뒤집어서 반환
    return answer[::-1]