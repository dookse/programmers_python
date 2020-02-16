# 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3


def solution(s):
    answer = []
    for word in s.split(' '):
        new_word = ''
        for idx, char in enumerate(word):
            new_word += char.upper() if idx % 2 == 0 else char.lower()
        answer.append(new_word)
    return ' '.join(answer)


print(solution('try hello world'))
print(solution('a  b  c'))
print(solution('  Ab  bc  cd  '))
