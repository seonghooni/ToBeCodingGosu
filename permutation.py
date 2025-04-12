
arr = [1, 2, 3, 4, 5, 6]
visited = [False] * len(arr)

def permutation(arr, n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutation(arr, n, new_arr + [arr[i]])
            visited[i] = False

def dupl_permutation(arr, n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        dupl_permutation(arr, n, new_arr + [arr[i]])

def combination(arr, n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combination(arr, n, new_arr + [arr[i]], i+1)

def dupl_combination(arr, n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        dupl_combination(arr, n, new_arr + [arr[i]], i)

# permutation(arr, 5, [])
# dupl_permutation(arr, 3, [])
# combination(arr, 3, [], 0)
dupl_combination(arr, 3, [], 0)
