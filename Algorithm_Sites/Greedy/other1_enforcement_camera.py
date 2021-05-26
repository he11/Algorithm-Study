def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 이동 경로의 진출점을 기준으로 오름차순으로 정렬한다
    last_camera = -30001

    for s, e in routes:
        if last_camera < s:
            answer += 1
            last_camera = e

    return answer