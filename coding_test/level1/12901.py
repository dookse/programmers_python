# 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3

from datetime import datetime


def solution(a, b):
    target_date = datetime(2016, a, b).date()
    return target_date.strftime('%a').upper()


print(solution(5, 24))
