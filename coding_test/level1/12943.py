# 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3


def solution(num):
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        cnt += 1
        if cnt == 500:
            return -1
    return cnt


print(solution(6))
print(solution(16))
print(solution(626331))
