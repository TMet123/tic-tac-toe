def printGrid(board, width, height):
    # Draw the game board
    for x in range(width):
        for y in range(height):
            if (y < 2):
                print(board[x][y], end='|')
            else:
                print(board[x][y], end='')
        print("")
