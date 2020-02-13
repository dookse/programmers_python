# 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3


def solution(x):
    s = sum(list(map(int, str(x))))
    print(s)
    return x % s == 0


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
