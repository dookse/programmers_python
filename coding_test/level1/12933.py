# 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3


def solution(n):
    return int(''.join(reversed(sorted(str(n)))))


print(solution(118372))
