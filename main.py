import random

slots = ["  " for i in range(9)]
player_1_wins = player_2_wins = tie = computer_wins = computer_turns = 0
WINNING_COMBINATIONS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def tic_tac_board(player, player_choice):
    global slots
    if player_choice:
        if player == 1:
            slots[player_choice - 1] = " O"
        elif player == 2 or player == 3:
            slots[player_choice - 1] = " X"

    print(f"\t\t\t\t\t\t\t {slots[0]} | {slots[1]} | {slots[2]} \n\t\t\t\t\t\t\t______________\n"
          f"\t\t\t\t\t\t\t {slots[3]} | {slots[4]} | {slots[5]} \n\t\t\t\t\t\t\t______________\n"
          f"\t\t\t\t\t\t\t {slots[6]} | {slots[7]} | {slots[8]} ")

def get_choice_input(choice_list):
    while True:
        c = input("Enter your choice: ")
        if c.isdigit() and int(c) in choice_list:
            return int(c)
        else:
            print(f"Invalid choice. Please choose b/w {choice_list[0]}-{choice_list[-1]}")

def get_empty_slots():
    return [i for i in range(9) if slots[i] == "  "]

def easy_mood_choose_randomly():
    return random.choice(get_empty_slots()) + 1  # computer selecting randomly empty slot

def get_slots(position):
    return [i for i in range(9) if slots[i] == position]
def check_must_in_slot(combination, slot_check):
    must_slot = [i for i in combination if i not in slot_check][0]
    if must_slot in get_empty_slots():
        return must_slot + 1
def hard_mood_using_ai():
    global computer_turns
    computer_turns += 1
    empty_slots = get_empty_slots()
    player_slots = get_slots(" O")
    computer_slots = get_slots(" X")

    if computer_turns == 1:
        return 5 if 4 in empty_slots else random.choice([0, 2, 6, 8]) + 1

    if computer_turns == 2:
        for combination in WINNING_COMBINATIONS:
            if player_slots[0] in combination and player_slots[1] in combination:
                must_slot = check_must_in_slot(combination, player_slots)
                if must_slot:
                    return must_slot
        else:
            return random.choice(get_empty_slots()) + 1  # for extra hard win send these to corners if player 1 is in center

    if computer_turns == 3:
        for combination in WINNING_COMBINATIONS:
            if computer_slots[0] in combination and computer_slots[1] in combination:
                must_slot = check_must_in_slot(combination, computer_slots)
                if must_slot:
                    return must_slot
        for combination in WINNING_COMBINATIONS:
            if (player_slots[0] in combination and player_slots[1] in combination) or (player_slots[0] in combination and player_slots[2] in combination) or (player_slots[1] in combination and player_slots[2] in combination):
                must_slot = check_must_in_slot(combination, player_slots)
                if must_slot:
                    return must_slot
        return random.choice(empty_slots) + 1

    if computer_turns == 4:
        for combination in WINNING_COMBINATIONS:
            if (computer_slots[0] in combination and computer_slots[1] in combination) or (computer_slots[0] in combination and computer_slots[2] in combination) or (computer_slots[1] in combination and computer_slots[2] in combination):
                must_slot = check_must_in_slot(combination, computer_slots)
                if must_slot:
                    return must_slot
        for combination in WINNING_COMBINATIONS:
            if (player_slots[0] in combination and player_slots[1] in combination) or (player_slots[0] in combination and player_slots[2] in combination) or (player_slots[0] in combination and player_slots[3] in combination) or (player_slots[1] in combination and player_slots[2] in combination) or (player_slots[1] in combination and player_slots[3] in combination) or (player_slots[2] in combination and player_slots[3] in combination):
                must_slot = check_must_in_slot(combination, player_slots)
                if must_slot:
                    return must_slot
        return random.choice(empty_slots) + 1


def check_valid_choice(player, mood=0):
    if player == 1:
        print("PLAYER 1.", end=" ")
    elif player == 2:
        print("PLAYER 2.", end=" ")
    if player == 3:  # computer
        print("COMPUTER CHOOSE:")
        if mood == 1:
            return easy_mood_choose_randomly()
        elif mood == 2:
            return hard_mood_using_ai()
    player_choice = 0
    while not player_choice:
        choice_ = get_choice_input(choice_list=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        if slots[choice_ - 1] == "  ":
            player_choice = choice_
        else:
            print("This box is already taken! Please try again!", end=" ")
    return player_choice

def goal(val, player):
    for combination in WINNING_COMBINATIONS:
        if all(slots[i] == val for i in combination):
            global player_1_wins, player_2_wins, computer_wins
            if player == 1:
                player_1_wins += 1
            elif player == 2:
                player_2_wins += 1
            elif player == 3:
                computer_wins += 1
                print(f"\nCOMPUTER WINSSS. TRY HARD!")
                return True
            print(f"\nPLAYER {player} WINSSS. CONGRATS")
            return True
    return False

def match_tie():
    global tie
    if not [i for i in range(9) if slots[i] == "  "]:
        print("\nMATCH TIE")
        tie += 1
        return True
    return False

def show_result(user):
    if user == "COMPUTER":
        print(
            f"\t\t\t\t\t-----------------------------\n\t\t\t\t\t| PLAYER 1 | {user} | TIE |\n\t\t\t\t\t|\t  {player_1_wins}    |\t {computer_wins}    |  {tie}\t|\n\t\t\t\t\t-----------------------------\n")
    else:
        print(
            f"\t\t\t\t\t-----------------------------\n\t\t\t\t\t| PLAYER 1 | {user} | TIE |\n\t\t\t\t\t|\t  {player_1_wins}    |\t {player_2_wins}    |  {tie}\t|\n\t\t\t\t\t-----------------------------\n")

def keep_continue():
    global slots
    continue_ = input("Do you want to continue (Y/N): ").upper()
    if continue_ in ["YES", "Y", "YEAH"]:
        slots = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
        return True
    else:
        print("Thanks for playing!")
        return False

def start_2_player_game():
    tic_tac_board(player=False, player_choice="")
    while True:
        # Player 1 turn
        tic_tac_board(player=1, player_choice=check_valid_choice(1))
        if goal(" O", 1):
            break
        if match_tie():
            break
        # PLAYER 2 TURN
        tic_tac_board(player=2, player_choice=check_valid_choice(2))
        if goal(" X", 2):
            break
    show_result("PLAYER 2")
    if keep_continue():
        start_2_player_game()
    else:
        return

def start_game_with_computer(computer_level):
    tic_tac_board(player=False, player_choice="")
    while True:
        # Player 1 turn
        tic_tac_board(player=1, player_choice=check_valid_choice(1))
        if goal(" O", 1):
            break
        if match_tie():
            break
        # COMPUTER TURN
        tic_tac_board(player=3, player_choice=check_valid_choice(3, computer_level))
        if goal(" X", 3):
            break
    show_result("COMPUTER")
    if keep_continue():
        global computer_turns
        computer_turns = 0
        start_game_with_computer(computer_level)
    else:
        return

print("Lets start the game!\n1. 2 Player Game\n2. Play with computer")
choice = get_choice_input(choice_list=[1, 2])
if choice == 2:
    print("Choose Level!\n1. Easy\n2. Hard")
    level = get_choice_input(choice_list=[1, 2])
    start_game_with_computer(level)
else:
    start_2_player_game()