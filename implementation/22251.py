import sys
input = sys.stdin.readline
N, K, P, X = map(int, input().split())

nums = [[False] * 7 for _ in range(10)]

# 숫자입력
nums[0] = [True] * 7
nums[0][6] = False
nums[1][1] = nums[1][2] = True
nums[2][0] = nums[2][1] = nums[2][3] = nums[2][4] = nums[2][6] = True
nums[3][0] = nums[3][1] = nums[3][2] = nums[3][3] = nums[3][6] = True
nums[4][1] = nums[4][2] = nums[4][5] = nums[4][6] = True
nums[5][0] = nums[5][2] = nums[5][3] = nums[5][5] = nums[5][6] = True
nums[6][0] = nums[6][2] = nums[6][3] = nums[6][4] = nums[6][5] = nums[6][6] = True
nums[7][0] = nums[7][1] = nums[7][2] = True
nums[8] = [True] * 7
nums[9] = [True] * 7
nums[9][4] = False

# 각 자릿수 별로 얼마나 바꿀 수 있는지 계산해놓은 배열
available_count = [[0] * 10 for _ in range(K)] # K = 1 이라면 하나밖에 생성 안하도록

# for i in range(N+1):

#
# 각 자릿수 별로 바꾸려면 얼마나 소모되는지 개수 계산
for decimal in range(K):
    val = ( X // 10**decimal ) % 10 # 각 자리수별 숫자 구하기
    # print(f'10 * {decimal}자리의 숫자는 {val}:', end =" ")
    for i in range(10):
        count = 0
        for j in range(7):
            if nums[val][j] != nums[i][j]:
                count += 1
        available_count[decimal][i] = count
    # print(available_count[decimal])


result = 0
# 3자리수를 기준으로 할때,
def dfs(k, total_count, num): # k번째 자리
    if num > N:
        return

    if k == 0:
        if num != X and num >= 1:
            global result
            result += 1
            # print(f'totalcount: {total_count}, num: {num}')
        return

    decimal = k-1

    for i in range(10):
        if available_count[decimal][i] + total_count <= P:
            dfs(k-1, available_count[decimal][i] + total_count, num + i * (10 ** decimal))


dfs(K, 0, 0)

print(result)