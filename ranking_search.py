from collections import defaultdict as dd
from bisect import bisect_left


def solution(info, query):
    answer = []
    # 후보 목록
    # <언어><직군><경력><소울푸드> 가 키값이 된다
    cand = dd(list)

    # 지원자 정보 전처리
    for i in info:
        # <언어><직군><경력><소울푸드> 를 키값으로 하여 딕셔너리에 후보들의 점수를 저장
        # - 쿼리에도 대응할 수 있도록 각 항목을 -로 한 키에도 저장해둔다.
        a, b, c, d, score = i.split()
        score = int(score)
        for u in [a, '-']:
            for v in [b, '-']:
                for w in [c, '-']:
                    for x in [d, '-']:
                        cand[u + v + w + x].append(score)

    # 각 키 값에 해당하는 점수 리스트를 오름차순 정렬
    for key in cand:
        cand[key].sort()

    # 질의 처리
    for i in query:
        a, b, c, d, score = i.replace('and', '').split()
        score = int(score)

        # 쿼리에 해당하는 키값으로 점수 리스트 hits 를 가져와 이분탐색으로 score 보다 크거나 같은 점수의
        # 인덱스를 구한다. hits 의 길이에서 이분탐색으로 구한 인덱스를 빼주면 조건에 해당하며 점수가 score
        # 이상인 지원자 수를 구할 수 있다.
        hits = cand[a + b + c + d]
        answer.append(len(hits) - bisect_left(hits, score))

    return answer
