n, k = map(int, input().split())

array = []
count = 0

for i in range(n):
    array.append(int(input()))

for i in range(n-1, -1, -1):
    if array[i] <= k:
        count += k // array[i]
        k = k % array[i]

        if k == 0 or i == 0:
            break

print(count)