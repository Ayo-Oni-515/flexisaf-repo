from random import randrange


board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

# This list stores the set of numbers removed from the board list
used = [5]


def display_board(board: list) -> None:
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""
       |       |
   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}
       |       |
+------|-------|-------+
       |       |
   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}
       |       |
+------|-------|-------+
       |       |
   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}
       |       |
    """)


def enter_move(board: list) -> None:
    # The function accepts the board's current status,
    # asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    user_input = int(input("Enter your move: "))
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == user_input:
                used.append(user_input)
                board[i][j] = "O"
                break


# def make_list_of_free_fields(board):
#     # The function browses the board and builds
#     # a list of all the free squares;
#     # the list consists of tuples, while each tuple
#     # is a pair of row and column numbers.
#     used = []
#     free = []
#     for i in range(len(board)):
#         for j in range(3):
#             if board[i][j] == "X" or board[i][j] == "O":
#                 new = (i, j)
#                 used.append(new)
#             else:
#                 new = (i, j)
#                 free.append(new)
#     return used


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for a in range(len(board)):
        if sign == board[a][0] and sign == board[a][1] and sign == board[a][2]:
            return True
        elif sign == (
                board[0][a] and sign == board[1][a] and sign == board[2][a]):
            return True
    if sign == board[0][0] and sign == board[1][1] and sign == board[2][2]:
        return True
    elif sign == board[0][2] and sign == board[1][1] and sign == board[2][0]:
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    computer_input = randrange(1, 10)
    while computer_input in used:
        computer_input = randrange(1, 10)
        if len(used) == 9:
            break
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == computer_input:
                used.append(computer_input)
                board[i][j] = "X"
                break


move = 1
display_board(board)
while move < 5:
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("You Won.")
        display_board(board)
        break
    draw_move(board)
    if victory_for(board, "X"):
        print("Computer Won.")
        display_board(board)
        break
    display_board(board)
    move += 1
if not victory_for(board, "O") and not victory_for(board, "X"):
    print("Game Inconclusive")
