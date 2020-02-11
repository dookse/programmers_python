# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3


def solution(arr1, arr2):
    result = []
    for a, b in zip(arr1, arr2):
        child = []
        for x, y in zip(a, b):
            child.append(x + y)
        result.append(child)
    return result


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
