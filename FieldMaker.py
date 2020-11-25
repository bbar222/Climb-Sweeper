import numpy as np

field = []

tiles = {"mine":-1,"empty":0}


def newBoard(ROWSIZE, MINEDENSITY):
    global field
    field = np.random.randint(0, 101, (ROWSIZE, 8))

    for row in range(field.shape[0]):
        for col in range(field.shape[1]):
            if field[row][col] >= MINEDENSITY:
                field[row][col] = tiles.get("mine")
            else:
                field[row][col] = tiles.get("empty")

    def checkAbove(r, c):
        if r != 0:
            if c != 0:
                if field[r - 1][c - 1] == tiles.get("mine"):
                    field[r][c] += 1
            if field[r - 1][c] == tiles.get("mine"):
                field[r][c] += 1
            if c != 7:
                if field[r - 1][c + 1] == tiles.get("mine"):
                    field[r][c] += 1

    def checkSides(r, c):
        if c == 0:
            if field[r][c + 1] == tiles.get("mine"):
                field[r][c] += 1
        elif c == 7:
            if field[r][c - 1] == tiles.get("mine"):
                field[r][c] += 1
        else:
            if field[r][c - 1] == tiles.get("mine"):
                field[r][c] += 1
            if field[r][c + 1] == tiles.get("mine"):
                field[r][c] += 1

    def checkBelow(r, c):
        if r != ROWSIZE - 1:
            if c != 0:
                if field[r + 1][c - 1] == tiles.get("mine"):
                    field[r][c] += 1
            if field[r + 1][c] == tiles.get("mine"):
                field[r][c] += 1
            if c != 7:
                if field[r + 1][c + 1] == tiles.get("mine"):
                    field[r][c] += 1

    for row in range(field.shape[0]):
        for col in range(field.shape[1]):

            if field[row][col] == tiles.get("mine"):
                # Do not need to check as there is a mine here
                # print("found a mine. skipping")
                continue

            # Check Above
            checkAbove(row, col)
            # Check left and right
            checkSides(row, col)
            # Check below
            checkBelow(row, col)

    # # Print the board
    # for ro in field:
    #     for co in ro:
    #         print(co,end="\t")
    #     print()

    print(field)

    return field





