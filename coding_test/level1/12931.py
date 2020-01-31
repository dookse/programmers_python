# 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3


def solution(n):
    return sum(map(int, str(n)))


print(solution(123))
print(solution(987))
