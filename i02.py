def solution(s):
    answer = []
    numbers = list(map(int, (s.replace('{', '').replace('}', '').replace(',', ' ')).split()))
    answer = [0 for _ in range(len(set(numbers)))]
    for num in numbers:
        if(num not in answer):
            answer[numbers.count(num)-1] = num
    
    return answer[::-1]