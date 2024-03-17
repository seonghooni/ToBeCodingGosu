n = input()

if not '0' in n:
    print(-1)
    exit()

sum_of_each_number = 0

for i in range(len(n)):
    sum_of_each_number += int(n[i])

if sum_of_each_number % 3 != 0:
    print(-1)
    exit()

result = sorted(n, reverse=True)
result = "".join(result)

print(result)