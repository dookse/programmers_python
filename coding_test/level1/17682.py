# 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682
import re
import unittest

bonus_dict = {'S': 1, 'D': 2, 'T': 3}


def solution(dart_result):
    scores = []
    exp = re.compile('\d*[SDT][*#]?')
    darts = exp.findall(dart_result)
    for dart in darts:
        text = dart
        score, bonus = get_score_bonus(text)
        score = score ** bonus_dict[bonus]
        score = check_option(score, scores, text)
        scores.append(score)
    return sum(scores)


def get_score_bonus(text):
    return int(re.match('\d*', text).group()), re.search('[SDT]', text).group()


def check_option(score, scores, text):
    option_serach = re.search('[*#]', text)
    if option_serach:
        option = option_serach.group()
        if option == '*':
            if scores:
                scores[len(scores) - 1] *= 2
            score *= 2
        else:
            score *= -1
    return score


class Test(unittest.TestCase):
    def test1(self):
        result = solution('1S2D*3T')
        self.assertEqual(37, result)

    def test2(self):
        result = solution('1D2S#10S')
        self.assertEqual(9, result)

    def test3(self):
        result = solution('1D2S0T')
        self.assertEqual(3, result)

    def test4(self):
        result = solution('1S*2T*3S')
        self.assertEqual(23, result)

    def test5(self):
        result = solution('1D#2S*3S')
        self.assertEqual(5, result)

    def test6(self):
        result = solution('1T2D3D#')
        self.assertEqual(-4, result)

    def test7(self):
        result = solution('1D2S3T*')
        self.assertEqual(59, result)


if __name__ == '__main__':
    unittest.main()
