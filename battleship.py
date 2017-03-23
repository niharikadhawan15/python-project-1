from random import randint


# The method 'game' asks the player for the difficulty level of the game which is by default 3.
def game():
    a = raw_input("Enter the difficulty level 1,2,3")
    if a == '1':
        boards = []
        for x in range(0, 3):
            boards.append(["O"] * 3)

    elif a == '2':
        boards = []
        for x in range(0, 4):
            boards.append(["O"] * 4)

    else:
        boards = []
        for x in range(0, 5):
            boards.append(["O"] * 5)


            # The method 'print_board' accept the board matrix and prints it.

    def print_board(boards):
        for row in boards:
            print " ".join(row)

    print "Let's play Battleship!"
    print_board(boards)

    # The two methods 'random_row' and 'random_col'accept the board matrix and return a random row or column from the board matrix.
    def random_row(boards):
        return randint(0, len(boards) - 1)

    def random_col(boards):
        return randint(0, len(boards[0]) - 1)

    ship_row = random_row(boards)
    ship_col = random_col(boards)

    # The loop gives the user 4 tries to guess the location of the ship.
    for turn in range(4):
        print "Turn", turn + 1
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            break;
        else:
            if (guess_row < 0 or guess_row > len(boards) - 1) or (guess_col < 0 or guess_col > len(boards) - 1):
                print "Oops, that's not even in the ocean."
            elif (boards[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                boards[guess_row][guess_col] = "X"
                # Print (turn + 1) here!
                print "Turn", turn + 1
                print_board(boards)
                if turn == 3:
                    print "Game Over"

    print "\n\nship_row is ", ship_row
    print "ship_col is ", ship_col
    b = raw_input("\nDo you want to play the game again ,if yes then type y")
    if b == 'y' or b == 'Y':
        game()
    else:
        print "Game ended"


game()









