import sys

# 1. 아래는 ( n!/k!*(n-k)! ) % 100000007 을 직접 계산한 경우이다. 시간초과가 발생
# 2. 두번째 방법은 동적 프로그래밍을 사용하는 법인데, 이또한 메모리 초과 우려
# 3. 세번째 방법은 검색으로 알게 된 페르마 소정리

# n, k = map(int, sys.stdin.readline().split())
# dividend = 1
# divisor = 1
#
# if n-k > k:
#     i = 0
#     m = n
#     t = k
#     while i != k:
#         dividend *= m
#         divisor *= t
#         m -= 1
#         t -= 1
#         i += 1
#     print((dividend // divisor) % 1000000007)
# else:
#     i = 0
#     m = n
#     t = n-k
#     while i != n-k:
#         dividend *= m
#         divisor *= t
#         m -= 1
#         t -= 1
#         i += 1
#     print((dividend // divisor) % 1000000007)


n, k = map(int, sys.stdin.readline().split())
p = 1000000007

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = n * i % p
    return n

def power(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        tmp = power(n, k//2)
        if k % 2:
            return tmp * tmp * n % p
        else:
            return tmp * tmp % p

# (A/B) % P = (A % P)(B^[P-2] % P) % P
A = factorial(n)
B = factorial(n-k) * factorial(k) % p
answer = A * power(B, p-2) % p

print(answer)