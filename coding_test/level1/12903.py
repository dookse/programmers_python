# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3


def solution(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]


print(solution('abcde'))
print(solution('qwer'))
