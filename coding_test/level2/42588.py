# 탑
# https://programmers.co.kr/learn/courses/30/lessons/42588
import unittest


def solution(heights):
    n = len(heights)
    answer = [0] * n
    for i in reversed(range(n)):
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j + 1
                break
    return answer


class Test(unittest.TestCase):
    def test1(self):
        result = solution([6, 9, 5, 7, 4])
        self.assertEqual([0, 0, 2, 2, 4], result)

    def test2(self):
        result = solution([3, 9, 9, 3, 5, 7, 2])
        self.assertEqual([0, 0, 0, 3, 3, 3, 6], result)

    def test3(self):
        result = solution([1, 5, 3, 6, 7, 6, 5])
        self.assertEqual([0, 0, 2, 0, 0, 5, 6], result)
