# 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3


def solution(s, n):
    codes = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    s = list(s)
    for i in range(len(s)):
        code = s[i].lower()
        if code not in codes:
            continue

        encoded_code = codes[(codes.index(code) + n) % 26]
        if s[i].isupper():
            s[i] = encoded_code.upper()
        else:
            s[i] = encoded_code.lower()
    return ''.join(s)


print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))
