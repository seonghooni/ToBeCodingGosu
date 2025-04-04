import sys
input = sys.stdin.readline

whole_str = input().strip()
exploit_str = input().strip()

stack = []
for char in whole_str:
    stack.append(char)

    if "".join(stack[-len(exploit_str):]) == exploit_str:
        for _ in range(len(exploit_str)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")


# index = 0
# while True:
#     index_reset = False
#     if index < 0:
#         index += 1
#         continue
#
#     for i in range(len(exploit_str)):
#         if index + i >= len(whole_str): # 범위 초과시 생략
#             break
#
#         if whole_str[index + i] == exploit_str[i]:
#             if i == len(exploit_str)-1: # 마지막 단어까지 일치한거라면
#                 # print(f'BOMB!!! index: {index}')
#                 # print(f'{whole_str} -> ', end= " ")
#                 whole_str = whole_str[:index] + whole_str[index+i+1:]
#                 # print(whole_str)
#                 index = index - len(exploit_str) + 1
#                 index_reset = True
#             continue # 일치할경우 다음문자까지 비교
#         else:
#             break # 일치하지 않을 경우 넘어감
#
#     if not index_reset:
#         index += 1
#
#     if index >= len(whole_str):
#         break
#
#
# if whole_str:
#     print(whole_str)
# else:
#     print("FRULA")