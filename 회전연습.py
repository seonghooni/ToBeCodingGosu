
arr = []

cnt = 10
for i in range(4):
    row = []
    for j in range(4):
        cnt += 1
        row.append(cnt)
    arr.append(row)

def print_arr(arr):
    for row in arr:
        print(row)
    print("----------")

print_arr(arr)

def partial_rotate(arr, start_x, start_y, length):
    new_arr = [row[:] for row in arr]
    for x in range(start_x, start_x+length):
        for y in range(start_y, start_y+length):
            ox = x - start_x
            oy = y - start_y
            rx = oy
            ry = length - 1 - ox
            new_arr[rx+start_x][ry+start_y] = arr[x][y]

    print_arr(new_arr)

partial_rotate(arr, 0, 1, 3)