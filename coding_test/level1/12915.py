# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3


def solution(strings, n):
    return sorted(sorted(strings), key=lambda string: string[n])


print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))
