# 입력을 받고, 홀수개인 알파벳이 있다면, 따로 분리 (홀수개인 알파벳이 2개 이상이면 팰린드롬으로 만들수가 없다.)
# 따라서, 1. 짝수개인 알파벳을 절반으로 나눈다음, 사전순으로 정렬,
# 2. 사전순으로 정렬한 반쪽짜리 알파벳을 출력 + (홀수개인 알파벳이 있었다면 그 알파벳을 출력) +
# 사전순으로 정렬한 반쪽짜리 알파벳의 정반대를 출력

alphabet_list = list(input())

isOddExist = False # 홀수개인 알파벳이 이미 존재하는지 확인

dict = {}
half_string = ""
odd_alphabet = ""

for alphabet in alphabet_list:
    if alphabet in dict:
        dict[alphabet] += 1
    else:
        dict[alphabet] = 1

for alphabet, count in dict.items():
    if count % 2 == 1:
        if isOddExist:
            print("I'm Sorry Hansoo")
            exit()
        odd_alphabet = alphabet
        isOddExist = True
        count -= 1

    for _ in range(count // 2): # 반쪽짜리에 짝수개인 알파벳을 추가함
        half_string += alphabet

half_string = ''.join(sorted(half_string))

result = half_string + odd_alphabet + half_string[::-1]

print(result)