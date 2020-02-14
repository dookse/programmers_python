# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3


def solution(n):
    primes = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in primes:
            primes -= set(range(i * 2, n + 1, i))
    return len(primes)


print(solution(10))
print(solution(5))
