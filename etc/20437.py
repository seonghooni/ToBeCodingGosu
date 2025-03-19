import sys
input = sys.stdin.readline

test_cases = int(input())

for _ in range(test_cases):

    min_distance = 10002
    max_distance = 0

    alphabets_arr = list(input().strip())
    count = int(input())

    alphabets_dict = dict()

    for idx, val in enumerate(alphabets_arr):
        if val not in alphabets_dict:
            alphabets_dict[val] = [idx]
        else:
            # setdefault(val, []).append(idx) 로 간단하게 할 수 있음
            arr = alphabets_dict[val]
            arr.append(idx)
            alphabets_dict[val] = arr

    is_possible = False
    for key, value in alphabets_dict.items():
        length = len(value)
        if length >= count:
            is_possible = True
            for i in range(length - count + 1):
                distance = value[i + count-1] - value[i]
                if distance > max_distance:
                    max_distance = distance
                if distance < min_distance:
                    min_distance = distance

    if is_possible:
        print(f'{min_distance+1} {max_distance+1}')
    else:
        print(-1)
