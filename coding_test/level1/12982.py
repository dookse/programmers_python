# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3


def solution(d, budget):
    answer = 0
    for cost in sorted(d):
        if budget >= cost:
            answer += 1
            budget -= cost
    return answer


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
