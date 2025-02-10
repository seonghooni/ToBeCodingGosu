from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
operator_sum = list(map(int, input().split()))
operators = []


# 0 1 2 3
# + - x //
for i in range(4):
    count = operator_sum[i]
    operators.extend([i] * count)

max_ = -1000000000
min_ = 1000000000

operators_order = set(permutations(operators))


for order in operators_order:
    before = num[0]

    i = 0
    for operator in order:
        i += 1
        after = num[i]

        if operator == 0:
            before += after
        elif operator == 1:
            before -= after
        elif operator == 2:
            before *= after
        else:
            if before < 0:
                temp = (-before) // after
                before = -temp
            else:
                before //= after

    min_ = min(min_, before)
    max_ = max(max_, before)

print(max_)
print(min_)