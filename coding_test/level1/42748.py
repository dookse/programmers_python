# K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3


def solution(array, commands):
    answer = []
    for command in commands:
        start, end, i = command
        start, i = start - 1, i - 1
        answer.append(sorted(array[start:end])[i])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
