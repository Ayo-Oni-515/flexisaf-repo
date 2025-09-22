from random import randrange
import time
import sys
import copy

grid_reset: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
grid: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valid_moves: list = list(range(1, 10))

# This list stores the set of numbers removed from the grid
used = []


def display_grid() -> None:
    """
    Dispalys the grid on the console

    Args:
        grid (list): represents the positions on the grid

    Returns:
        None
    """
    global grid

    time.sleep(0.5)

    print(f"""
       |       |
   {grid[0][0]}   |   {grid[0][1]}   |   {grid[0][2]}
       |       |
+------|-------|-------+
       |       |
   {grid[1][0]}   |   {grid[1][1]}   |   {grid[1][2]}
       |       |
+------|-------|-------+
       |       |
   {grid[2][0]}   |   {grid[2][1]}   |   {grid[2][2]}
       |       |
    """)


def enter_move() -> None:
    """
    1. accepts the grid's current status
    2. asks the user about their move
    3. checks the input, and updates the grid
    according to the user's decision.

    Args:
        grid (list): represents the positions on the grid

    Returns:
        None
    """
    global grid, used

    while True:
        try:
            user_input = int(input("Enter your move: "))
            if ((user_input not in valid_moves) or
                    (user_input in used)):
                print("\n\t>>>Error: Invalid option!\n")
                continue
            break
        except Exception:
            print("\n\t>>>Error: Invalid option!\n")

    for i in range(len(grid)):
        for j in range(3):
            if grid[i][j] == user_input:
                used.append(user_input)
                grid[i][j] = "O"


def victory_for(sign: str) -> bool:
    """Determines game's victor

    Args:
        grid (list): represents the positions on the grid
        sign (str): possible game optons

    Returns:
        bool
    """
    global grid

    for a in range(len(grid)):
        if sign == grid[a][0] and sign == grid[a][1] and sign == grid[a][2]:
            return True
        elif (sign == grid[0][a] and
              sign == grid[1][a] and sign == grid[2][a]):
            return True
    if sign == grid[0][0] and sign == grid[1][1] and sign == grid[2][2]:
        return True
    elif sign == grid[0][2] and sign == grid[1][1] and sign == grid[2][0]:
        return True
    return False


def draw_move():
    """Draws the computer's move and updates the grid.

    Args:
        grid (list): represents the positions on the grid

    Retunrs:
        None
    """
    global grid

    computer_input = randrange(1, 10)

    while computer_input in used:
        computer_input = randrange(1, 10)

    for i in range(len(grid)):
        for j in range(3):
            if grid[i][j] == computer_input:
                used.append(computer_input)
                grid[i][j] = "X"


def reset_grid():
    global grid, used

    grid = copy.deepcopy(grid_reset)
    used.clear()


def game_play() -> None:
    global grid, used

    display_grid()
    while True:
        if len(used) == 9:
            print("Game Inconclusive")
            reset_grid()
            break

        draw_move()
        display_grid()
        if victory_for(sign="X"):
            print("Computer Won!")
            reset_grid()
            break

        if len(used) == 9:
            print("Game Inconclusive")
            reset_grid()
            break

        enter_move()
        display_grid()
        if victory_for(sign="O"):
            print("You Won!")
            reset_grid()
            break


if __name__ == "__main__":
    print("""
Welcome to my Tic-Tac-Toe program!

Instructions:
    1. Enter value corresponding to chosen position.
    2. Type 'n' to quit when prompted for a new game.
    """)

    while True:
        game_play()

        while True:
            try:
                new_game: str = input("\nNew game? 'y' or 'n': ")
                if new_game.lower() == "n":
                    sys.exit(0)
                elif new_game.lower() == "y":
                    reset_grid()
                    break
                else:
                    raise Exception
            except Exception:
                print("\n\t>>>Error: Invalid option!")
