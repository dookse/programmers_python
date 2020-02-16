# x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3


def solution(x, n):
    return [i * x + x for i in range(n)]


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
print(solution(-10000000, 1000))
print(solution(10000000, 1000))
print(solution(0, 5))
