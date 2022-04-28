'''
매개변수는 2차원 문자열 배열 places
    places의 행 길이(대기실 개수) = 5
    places의 각 행은 하나의 대기실 구조
    places의 열 길이(대기실 세로 길이) = 5
    places의 원소는 P,O,X로 이루어진 문자열
    P는 응시자가 앉아있는 자리를 의미
    O는 빈 테이블을 의미
    X는 파티션을 의미
return 값 형식
    1차원 정수 배열에 5개의 원소를 담아서 return
    places에 담겨 있는 5개 대기실의 순서대로 거리두기 준수 여부를 차례대로 배열에 담음
    거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말 것
    단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용
    각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담음
맨해튼 거리
    두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면
    T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2|
'''
def solution(places):
    answer = []
    for i in range(len(places)) :
        room = places[i]

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

answer = solution(places)
print(answer)