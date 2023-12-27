def vertical_flip(arr):
    arr[0][0], arr[0][1] = arr[0][1], arr[0][0]
    arr[1][0], arr[1][1] = arr[1][1], arr[1][0]

def horizontal_flip(arr):
    arr[0][0], arr[1][0] = arr[1][0], arr[0][0]
    arr[0][1], arr[1][1] = arr[1][1], arr[0][1]

grid = [["1", "2"], ["3", "4"]]

directions = input()

for direction in directions:
    if direction == "H":
        horizontal_flip(grid)
    else:
        vertical_flip(grid)

for i in grid:
    print(" ".join(i))
