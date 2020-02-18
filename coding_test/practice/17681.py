# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681
import unittest


def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        result = bin(a | b)[2:].zfill(n)
        result = result.replace('0', ' ').replace('1', '#')
        answer.append(result)
    return answer


class Test(unittest.TestCase):
    def test_solution1(self):
        result = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
        self.assertEqual(['#####', '# # #', '### #', '#  ##', '#####'], result)

    def test_solution2(self):
        result = solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
        self.assertEqual(['######', '###  #', '##  ##', ' #### ', ' #####', '### # '], result)


if __name__ == '__main__':
    unittest.main()
