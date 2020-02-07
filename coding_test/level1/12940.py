# 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3
import math


def solution(n, m):
    return [math.gcd(n, m), lcm(n, m)]


def lcm(n, m):
    return abs(n * m) // math.gcd(n, m)


print(solution(1000000, 100000))
print(solution(11, 13))
print(solution(12, 3))
print(solution(2, 3))
print(solution(1, 1))
print(solution(3, 12))
print(solution(2, 5))
print(solution(10, 30))
print(solution(22, 792))
