# 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3
import math


def solution(n):
    root = math.sqrt(n)
    if int(root) == root:
        return int(root + 1) ** 2
    else:
        return -1


print(solution(121))
print(solution(3))
