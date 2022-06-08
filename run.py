import gspread
from google.oauth2.service_account import Credentials
import quiz


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('music_quiz')

# title message
print("Welcome to my Music Quiz!\n")
print("Think you know all things music?\n")
print("Test yourself with this 10 question quiz!\n")


# 3 different options to choose from
def game_menu():
    """
    game menu options
    play, restart and quit
    """
    print("\n")
    print("Click 1-3 to choose from the options below:")
    print("1. Play \n2. Restart \n3. Quit \n")


# different outcomes for each option
    while True:
        menu_choice = input("Please choose an option below. \n").strip()
        print("\n")

        if menu_choice == "1":
            print("Class! Lets get rocking!\n")
            break
        elif menu_choice == "2":
            print("Let's go again!")
            restart_game()
        elif menu_choice == "3":
            print("Okay, see you next time!")
        else:
            print("Invalid input! Please choose between 1 - 3")


# player enters name
def enter_player_name():
    """
    allows user to enter
    their name
    """
    while True:
        print("Next choose a username!\n")
        print("Letters A-Z, a-z, and numbers 0-9 are allowed.")
        print("Maximum of 8 characters.")
        print("Any white space will be removed.\n")

        player_name = input("Please enter your chosen username: \n")

        if check_name(player_name):
            print("\n")
            print(f"Hi {player_name}, lets get ready to rock! \n")
            print("This is a multiple choice quiz.")
            print("Enter 'A', 'B' or 'C' to choose your answer.")
            print("Letters are not case-sensitive.\n")
            print("Go forth and smash it!\n")
            data = quiz.play_quiz()
            game_menu()

    check_name(player_name)
    return player_name.strip()


def check_name(player_name):
    """
    checks if username meets standards
    will raise ValueError if its more
    than 8 characters, no name entered
    if special characters used
    """
    try:
        if not player_name:
            raise ValueError("Please enter a username!")
        if len(player_name) > 8:
            raise ValueError("Oops! Username too long.")
        if not player_name.isalnum():
            raise ValueError("Only letters and numbers are allowed")
    except ValueError as error:
        print(f"Invalid data: {error}! Please try again.\n")
        return False

    return True


def restart_game():
    """
    allow player to restart the game
    """
    while True:
        data = quiz.play_quiz()
        game_menu()


def main():
    """
    Run all the functions for the game
    """
    game_menu()
    enter_player_name()


main()
