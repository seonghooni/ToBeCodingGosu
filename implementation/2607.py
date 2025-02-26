N = int(input())


# base_word 딕셔너리 구성
base_word = input()
base_dict = dict()
for alphabet in base_word:
    if alphabet in base_dict: # key가 있으면
        base_dict[alphabet] = base_dict[alphabet] + 1
    else: # key가 없으면
        base_dict[alphabet] = 1


result = 0

for _ in range(N-1):
    # target_word 딕셔너리 구성
    target_word = input()
    target_dict = dict()

    for alphabet in target_word:
        if alphabet in target_dict:  # key가 있으면
            target_dict[alphabet] = target_dict[alphabet] + 1
        else:  # key가 없으면
            target_dict[alphabet] = 1

    # 하나씩 소거해보자
    target_dict_copy = target_dict.copy()
    base_dict_copy = base_dict.copy()

    all_keys = target_dict_copy.keys()

    for key in all_keys:
        if key in base_dict_copy: # 기준 dict에 있으면
            base_dict_copy[key] = base_dict_copy[key] - target_dict_copy[key]
            if base_dict_copy[key] <= 0:
                base_dict_copy.pop(key)
        first_count = sum(base_dict_copy.values())

    # 반대로 소거해보자
    target_dict_copy = target_dict.copy()
    base_dict_copy = base_dict.copy()

    all_keys = base_dict_copy.keys()
    second_count = 0

    for key in all_keys:
        if key in target_dict_copy: # 기준 dict에 있으면
            target_dict_copy[key] = target_dict_copy[key] - base_dict_copy[key]
            if target_dict_copy[key] <= 0:
                target_dict_copy.pop(key)
        second_count = sum(target_dict_copy.values())

    if first_count <= 1 and second_count <= 1:
        result += 1

print(result)