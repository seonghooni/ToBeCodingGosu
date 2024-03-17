N = int(input())

remainder = N
num = 1

used_num = []

while True:
    remainder = remainder - num
    used_num.append(num)
    if remainder == 0:
        break

    if remainder <= num:
        before_num = used_num.pop()
        remainder += before_num

    num += 1

print(len(used_num))

