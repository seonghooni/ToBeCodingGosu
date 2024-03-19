# 역으로 계산하면서 경우의 수를 따져본다.
#
# while (A < B)
#     if) 일의자리 숫자가 1이면
#         일의자리 숫자를 지우고, 정수로 변환 (카운트 + 1)
#     else) 일의자리 숫자가 1이 아니면
#         if) 1이 아닌 홀수이면
#            -1 리턴
#         else) 1이 아닌 짝수이면
#         	2로 나눈다 (카운트 + 1)
#
# 만약 A > B 이면 만들수가 없으므로 -1 리턴
# A == B 이면 결과 출력


A, B = map(int, input().split())

result = 1

# 일의 자리 숫자가 1인지를 알고싶으면 9를 더해봤을 때 일의 자리 숫자가 0이 되는지 확인
while A<B:
    B = B+9
    if B % 10 == 0: # 일의 자리 숫자가 1이면
        B = B-9
        B = B//10
    else:
        B = B-9
        if B%2 == 1:
            print(-1)
            exit(0)
        else:
            B = B//2
    result = result+1

if A>B:
    print(-1)
    exit(0)

print(result)