# 매우 어려웠던 문제 (정답률을 보고 골드문제일줄 알았으나 다이아문제라고 한다.)
# 가능한 한 3개씩 무조건 빼기만 하면 될 줄 알았는데, i+1과 i+3이 고립되는 경우 비용이 더 책정되는 것을 고려해야 한다.
# 따라서, 우선적으로 A[i+1] > A[i+2] 인지 먼저 판단해야 하고
#        그 이후에 A[i] 와 A[i+1] - A[i+2]를 비교하여, 더 작은 값을 기준으로 2개씩(cost=5) 뺀 후에
#        3개씩(cost=7) 빼야 한다.
# 혼자서 못 풀었기 때문에 블로그 글을 참고했다. https://jjunohj.github.io/boj/boj-18185/

num = int(input())

A = list(map(int, input().split())) + [0, 0]

cost = 0

i = 0

for i in range(num):
    if A[i+1] > A[i+2]:
        minimum = min(A[i], A[i + 1] - A[i + 2])
        A[i] -= minimum
        A[i+1] -= minimum
        cost += minimum * 5

        minimum = min(A[i], A[i + 1], A[i + 2])
        A[i] -= minimum
        A[i+1] -= minimum
        A[i+2] -= minimum
        cost += minimum * 7

    else:
        minimum = min(A[i], A[i + 1], A[i + 2])
        A[i] -= minimum
        A[i + 1] -= minimum
        A[i + 2] -= minimum
        cost += minimum * 7

        minimum = min(A[i], A[i + 1])
        A[i] -= minimum
        A[i + 1] -= minimum
        cost += minimum * 5
    cost += A[i] * 3
    A[i] = 0

print(cost)