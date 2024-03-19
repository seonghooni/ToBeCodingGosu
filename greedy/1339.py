# 1. 딕셔너리를 이용해, 각 자릿값만큼 value값을 더하여 관리해준다
# 2. value값을 기준으로 정렬하고
# 3. 내림차순으로 9부터 차례대로 곱해서 result에 더해준다.

N = int(input())

str_list = []
alphabet_dic = {}

char_number = 65
for i in range(26):
    alphabet_dic[chr(char_number)] = 0
    char_number += 1

value_list = []
result = 0

# 문자열을 입력받아 추가함
for _ in range(N):
    str_list.append(input())

# 1. 딕셔너리를 이용해, 각 자릿값만큼 value값을 더하여 관리해준다
for string in str_list:
    for i in range(len(string)): # i는 0부터 시작
        key = string[i]
        current_value = alphabet_dic.get(key)
        alphabet_dic[key] = current_value + 10 ** (len(string) - i - 1) # (해당 자릿수)만큼 제곱하여 현재 딕셔너리 value값에 더함

# 2. value값을 기준으로 정렬하고
for value in alphabet_dic.values():
    if value > 0:
        value_list.append(value)

value_list.sort(reverse=True)

# 3. 내림차순으로 9부터 차례대로 곱해서 result에 더해준다.
i = 9
for value in value_list:
    result += value * i
    i -= 1

print(result)