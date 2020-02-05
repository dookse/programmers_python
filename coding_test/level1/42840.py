# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3


def solution(answers):
    ways = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0, 0, 0]

    for ans_idx, ans_val in enumerate(answers):
        for way_idx, way_val in enumerate(ways):
            if ans_val == way_val[ans_idx % len(ways[way_idx])]:
                scores[way_idx] += 1

    return [i + 1 for i, v in enumerate(scores) if v == max(scores)]


print(solution([i % 5 + 1 for i in range(10000)]))
print(solution([5, 1]))
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
print(solution([1, 3, 2, 5, 2]))
