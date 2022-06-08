def play_quiz():
    """
    quiz game - if player guesses
    correctly, score goes up by one
    """
    score = 0

# Q1
    while True:
        print("Which symbol was the title of Ed Sheerans first album?")
        ans1 = input("A. +\nB. =\nC. % /n Answer:\n").strip()
        if ans1.upper() == "A":
            print("Correct!\n")
            score += 1
            break
        elif ans1.upper() == "B" or ans1.upper() == "C":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q2
    while True:
        print("Which symbol was the title of Ed Sheerans first album?")
        ans1 = input("A. +\nB. =\nC. %/nAnswer:\n").strip()
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
    print("You scored" + "" + str(score) + "" + "out of 10!\n")

    # statement for success
    # or condolances message

    if score <= 4:
        print("You can do better than that, try again!\n")
        return score
    elif score > 4 and score <= 7:
        print("Great job!\n")
        return score
    else:
        print("Unreal, well done!\n")
        return score
