import sys
input = sys.stdin.readline

S = input()
T = input()


S = S[:-1]
T = T[:-1]

result = 0
def recursive(str_):
    global result

    if str_ == S:
        result = 1
        return

    if len(str_) == 0:
        return

    if str_[0] == 'B':
        recursive("".join(reversed(str_))[:-1])

    if str_[-1] == 'A':
        recursive(str_[:-1])

recursive(T)
print(result)
