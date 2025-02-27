H, W, N, M = map(int, input().split())

max_width_table = (W-1) // (M+1) + 1
max_height_table = (H-1) // (N+1) + 1

print(max_height_table * max_width_table)