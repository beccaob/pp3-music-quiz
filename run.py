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
print("To begin, just enter your name and lets get rocking!")

def menu():
# 4 different options to choose from
print("Click 1-4 to choose from the options below:")
print("1. Play \n2. Restart \n3. Scoreboard \n4. Quit")

# different outcomes for each option
while True:
    menu_choice = input("What would you like to do? \n").strip()
    print("\n")

    if menu_choice == "1":
        print("Class! Lets get rocking!\n")
        break
    elif menu_choice == "2":
        print("Let's go again!")
        # add restart game funct here 
    elif menu_choice == "3":
        # display scorebard func here
    elif menu_choice == "4":
        print("Aww :( See you next time!")
        # quit funct here 
    else:
        print("Invalid input! Please choose between 1 - 4")

