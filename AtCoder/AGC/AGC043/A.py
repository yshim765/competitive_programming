h, w = input().split()
h, w = int(h), int(w)

grid_state = []

# 1 = black, 0 = white

for _ in range(h):
    temp = [int(s) for s in input().replace(".", "0").replace("#", "1")]
    grid_state.append(temp)

grid_cost = [[0 for _ in range(w)] for _ in range(h)]

grid_cost[0][0] = grid_state[0][0]

for i in range(1, h + w - 1):
    j = i
    if j > w - 1:
        j = w - 1
    while((j >= 0) and (i - j < h)):
        if i - j == 0:
            if grid_state[i - j][j - 1] == 1:
                grid_cost[i - j][j] = grid_cost[i - j][j - 1]
            else:
                grid_cost[i - j][j] = grid_cost[i - j][j - 1] + grid_state[i - j][j]
        elif j == 0:
            if grid_state[i - j - 1][j] == 1:
                grid_cost[i - j][j] = grid_cost[i - j - 1][j]
            else:
                grid_cost[i - j][j] = grid_cost[i - j - 1][j] + grid_state[i - j][j]
        else:
            min_cost = min([grid_cost[i - j - 1][j], grid_cost[i - j][j - 1]])

            if grid_state[i - j][j] == 0:
                grid_cost[i - j][j] = min([grid_cost[i - j - 1][j], grid_cost[i - j][j - 1]])
            elif (grid_state[i - j - 1][j] == 1) and (grid_cost[i - j - 1][j] <= grid_cost[i - j][j - 1]):
                grid_cost[i - j][j] = min_cost
            elif (grid_state[i - j - 1][j] == 0) and (grid_cost[i - j - 1][j] < grid_cost[i - j][j - 1]):
                grid_cost[i - j][j] = min_cost + 1
            elif (grid_state[i - j][j - 1] == 1) and (grid_cost[i - j - 1][j] >= grid_cost[i - j][j - 1]):
                grid_cost[i - j][j] = min_cost
            else:
                grid_cost[i - j][j] = min_cost + 1

        j -= 1

print(grid_cost[h - 1][w - 1])