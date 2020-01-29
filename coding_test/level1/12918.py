# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3


def solution(s: str):
    return len(s) in (4, 6) and s.isnumeric()


print(solution('1234'))
print(solution('a234'))
print(solution('123456'))
print(solution('12345a'))
