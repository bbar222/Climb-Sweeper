import numpy as np

field = np.random.randint(0,101,(8,8))

mine = 'X'
empty = ' '

tiles = {"mine":-1,"empty":0}

for row in range(field.shape[0]):
    for col in range(field.shape[1]):
        if field[row][col] >= 80:
            field[row][col] = tiles.get("mine")
        else:
            field[row][col] = tiles.get("empty")





for row in range(field.shape[0]):
    localMines = 0
    for col in range(field.shape[1]):


        if field[row][col] == tiles.get("mine"):
            # Do not need to check as there is a mine here
            localMines = 0
            continue




        try:
            # Check row above
            if row > -1 and col - 1 > -1 and col + 1 < 8:
                if field[row-1][col-1] == tiles.get("mine"):
                    field[row][col] += 1
                if field[row-1][col] == tiles.get("mine"):
                    field[row][col] += 1
                if field[row-1][col+1] == tiles.get("mine"):
                    field[row][col] += 1
            # Check left and right
            if col - 1 > -1 and col + 1 < 8:
                if field[row][col-1] == tiles.get("mine"):
                    field[row][col] += 1
                if field[row][col+1] == tiles.get("mine"):
                    field[row][col] += 1
            # Check row below
            if row + 1 < 8 and col - 1 > -1 and col + 1 < 8:
                if field[row+1][col-1] == tiles.get("mine"):
                    field[row][col] += 1
                if field[row+1][col] == tiles.get("mine"):
                    field[row][col] += 1
                if field[row+1][col+1] == tiles.get("mine"):
                    field[row][col] += 1
        except IndexError:
            print("lol")
# Print the board
for r in field:
    for c in r:
        print(c,end = "\t")
    print()