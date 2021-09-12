def solution(play_time, adv_time, logs):
    # ① 광고의 재생시간이 영상의 재생시간과 같다면 영상의 첫 부분에 삽입하면 된다.
    if play_time == adv_time:
        return '00:00:00'

    # ② 영상 재생시간과 광고 재생시간을 초단위의 정수로 변환
    pt, at = stoh(play_time), stoh(adv_time)

    # ③ 시간별 재생횟수를 나타내기위한 타임라인 배열을 생성
    timeline = [0] * 360001

    # ④, ⑤ 로그를 분석하여 재생 시작시간과 종료시간을 구한 뒤
    # 누적 합을 활용하여 타임라인에 재생 횟수를 표기
    for log in logs:
        s, e = map(stoh, log.split('-'))
        timeline[s] += 1
        timeline[e] -= 1
    for i in range(1, 360001):
        timeline[i] += timeline[i - 1]

    # ⑦, ⑧ 영상의 시작시간부터 timeline의 at(광고 재생시간)크기의 구간합이 최대가 되는 경우를 탐색

    # 최대구간합 maxw, 정답으로 반환할 시작시간 answer
    maxw, answer = sum(timeline[:at]), 0

    # 초기 구간합 w = maxw
    w = maxw

    # 영상의 시작시간부터 탐색 시작
    for s in range(1, pt - at + 1):
        # 투 포인터를 활용하여 구간합을 갱신해나가는 방식을 사용
        w = w - timeline[s - 1] + timeline[s + at - 1]

        # 만약 새로운 구간합이 최대 구간합 maxw보다 크다면 maxw와 answer 갱신
        if w > maxw:
            maxw, answer = w, s

    # 광고를 삽입할 최적의 시작시간을 문자열로 변환하여 반환
    answer = htos(answer)
    return answer


# 문자열 형태의 시간을 초단위의 정수로 변환
def stoh(times):
    h, m, s = map(int, times.split(':'))
    return h * 3600 + m * 60 + s


# 초단위의 정수를 문자열 형태의 시간으로 변환
def htos(sec):
    h = sec // 3600
    sec %= 3600
    m = sec // 60
    s = sec % 60
    return '%02d:%02d:%02d' % (h, m, s)
