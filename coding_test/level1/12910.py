# 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3


def solution(arr, divisor):
    result = sorted([i for i in arr if i % divisor == 0])
    return result or [-1]


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))
