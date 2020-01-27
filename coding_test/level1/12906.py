# 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3


def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
print(solution([]))
print(solution([1, 2, 2, 2]))
