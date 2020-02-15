# 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3


def solution(arr):
    if len(arr) <= 1:
        return [-1]
    arr.remove(min(arr))
    return arr


print(solution([4, 3, 2, 1]))
print(solution([10]))
