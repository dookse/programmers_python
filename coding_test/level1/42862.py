# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3


def solution(n, lost, reserve):
    intersection = set(lost) & set(reserve)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)

    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    return n - len(lost)


# 5, 4, 2
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [4, 5, 6], [4, 5]))
