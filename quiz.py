# questions and answers of quiz game held here 

def play_quiz():

    score = 0 
# variable for score
# each time player gets question correct
# score will increase by 1

# Q1
while True:
    print("Which mathematical symbol was the title of Ed Sheerans first album in 2011?")
    ans1 = input("A. + \nB. = \nC. % /nAnswer: \n").strip()
    if ans1.upper() == "A":
        print("Correct!\n")
        score += 1
        break
    elif ans1.upper() == "B" or ans1.upper() == "C":
        print("Oops! That's incorrect.\n")
        break
    else: 
        print("Invalid answer! Please choose between A, B or C\n")

    # final score
    print("You scored" + str(score) + "out of 10!\n")

    # statement for success
    # or condolances message

    if score <= 4:
        print("You can do better than that, try again!\n")
        return score
    elif score > 4 and score <=7:
        print("Great job!\n") 
    else:
        print("Unreal, well done!")
        return score