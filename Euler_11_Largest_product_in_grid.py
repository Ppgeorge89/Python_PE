import time
import sys

try:
    start_time = time.time()

    filename = "20x20_grid.txt"
    file = open(filename, "r")
    text = file.read()
    numbers = list(map(int, text.split()))

    grid = [[] for i in range(0, 20)]

    for i in range(0, 20):
        for j in range(0, 20):
            grid[i].append(numbers[j + 20 * i])



    prod = []
    for i in range(0, 17):
        for j in range(0, 17):
            prod_left = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
            prod_down = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            prod_dia_1 = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            prod.append(prod_left)
            prod.append(prod_down)
            prod.append(prod_dia_1)
            print(grid[i][j], "x", grid[i + 1][j] ,"x", grid[i + 2][j] ,"x", grid[i + 3][j])
            print(grid[i][j] ,"x", grid[i][j + 1] ,"x", grid[i][j + 2] ,"x", grid[i][j + 3])
            print(grid[i][j] ,"x", grid[i + 1][j + 1] ,"x", grid[i + 2][j + 2] ,"x", grid[i + 3][j + 3])
            if i >= 3 and j <= 16:
                prod_dia_2 = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
                prod.append(prod_dia_2)
                print(grid[i][j] ,"x", grid[i + 1][j - 1] ,"x", grid[i + 2][j - 2] ,"x", grid[i + 3][j - 3])


    print(list(reversed(sorted(prod)))[0])
except TypeError:
    print("You did not insert a valid number...")
    sys.exit()
except UnboundLocalError:
    print("You did not insert a valid number...")
    sys.exit()

print("--- %s seconds ---" % (time.time() - start_time))