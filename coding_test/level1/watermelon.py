# 수박수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3


def solution(n):
    answer = '수박' * (n // 2 + 2)
    return answer[:n]


print(solution(3))
print(solution(4))
