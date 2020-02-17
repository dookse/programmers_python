# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
import collections


def solution(n, stages):
    stages_fail = collections.defaultdict(int)
    stages_access = collections.defaultdict(int)
    answer_dict = {}

    for stage in stages:
        stages_fail[stage] += 1
        for i in range(1, stage + 1):
            stages_access[i] += 1

    for i in range(1, n + 1):
        answer_dict[i] = stages_fail[i] / (stages_access[i] + 1e-10)

    return sorted(answer_dict, key=lambda x: answer_dict[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(1, [0]))
print(solution(1, [2]))
