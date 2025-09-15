from random import randrange


moves: dict = {
    1: "rocks",
    2: "paper",
    3: "scissors"
}


def computer_choice() -> int:
    return randrange(1, 4)


def your_choice():
    try:
        player_choice: int = int(input("Enter your choice: "))
        if player_choice not in range(1, 4):
            raise TypeError
        return player_choice
    except TypeError:
        print("\n\t>>>Error: Invalid choice range!")
    except ValueError:
        return None


def compare_choices(player, computer) -> str:
    if player == computer:
        return f"Draw: {moves[player]} same as {moves[computer]}!\n"
    else:
        if (player == 1) and (computer == 2):
            return f"Computer won: {moves[computer]} beats {moves[player]}!\n"
        elif (player == 1) and (computer == 3):
            return f"You won: {moves[player]} beats {moves[computer]}!\n"
        elif (player == 2) and (computer == 1):
            return f"You won: {moves[player]} beats {moves[computer]}!\n"
        elif (player == 2) and (computer == 3):
            return f"Computer won: {moves[computer]} beats {moves[player]}!\n"
        elif (player == 3) and (computer == 1):
            return f"Computer won: {moves[computer]} beats {moves[player]}!\n"
        elif (player == 3) and (computer == 2):
            return f"You won: {moves[player]} beats {moves[computer]}!\n"


def main():
    """main game loop"""
    while True:
        player: int = your_choice()
        if player is None:
            break
        computer: int = computer_choice()

        print(compare_choices(player, computer))


if __name__ == "__main__":
    print("""
            Welcome to my rocks-paper-scissors game!

Instructions:

1. The following values represent choices (1 for 'rocks'), (2 for 'paper'), and
(3 for 'scissors').
2. Enter values corresponding to your choice or type 'exit' to end game.
    """)
    main()
