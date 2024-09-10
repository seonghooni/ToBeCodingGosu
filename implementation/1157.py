# 딕셔너리 자료형으로 구현하고 싶다면,
# 1. alphabet_dict = {key_expression: value_expression for item in iterable}
# 2. sorted_keys = sorted(alphabet_dict, key=lambda k: alphabet_dict[k])

words = list(str.upper(input()))
max_index = 0
max_value = 0
is_duplicated = False

alphabet_arr = [0] * 91

for word in words:
    cur_index = ord(word)
    alphabet_arr[cur_index] += 1
    if max_value < alphabet_arr[cur_index]:
        max_index = cur_index
        max_value = alphabet_arr[cur_index]
        is_duplicated = False
    elif max_value == alphabet_arr[cur_index]:
        is_duplicated = True

if is_duplicated:
    print('?')
else:
    print(chr(max_index))
