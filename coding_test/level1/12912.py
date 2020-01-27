# 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3


def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
print(solution(1, 10))
