def play_quiz():
    """
    quiz game - if player guesses
    correctly, score goes up by one
    """
    score = 0

# Q1
    while True:
        print("Which symbol was the title of Ed Sheerans first album?")
        ans1 = input("A. +\nB. =\nC. %\n").strip()
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
        print("Which rock band was founded by Trent Reznor in 1988?")
        ans2 = input("A. ACDC\nB. Nine Inch Nails\nC. Queen\n").strip()
        if ans2.upper() == "B":
            print("Correct!\n")
            score += 1
            break
        elif ans1.upper() == "A" or ans1.upper() == "C":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q3
    while True:
        print("How many members are there in pop group Little Mix?")
        ans3 = input("A. 3\nB. 4\nC. 2\n").strip()
        if ans3.upper() == "A":
            print("Correct!\n")
            score += 1
            break
        elif ans1.upper() == "B" or ans1.upper() == "C":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q4
    while True:
        print("Which talent show judge managed Westlife?")
        ans4 = input("A. Bressie\nB. Simon Cowell\nC. Louis Walsh\n").strip()
        if ans4.upper() == "C":
            print("Correct!\n")
            score += 1
            break
        elif ans1.upper() == "B" or ans1.upper() == "A":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q5
    while True:
        print("Roger Taylor is the drummer in which band?")
        ans5 = input("A. Guns N Roses\nB. Queen\nC. Led Zeppelin\n").strip()
        if ans5.upper() == "B":
            print("Correct!\n")
            score += 1
            break
        elif ans1.upper() == "C" or ans1.upper() == "A":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q6
    while True:
        print("Which Bob Dylan song did Adele include on her first album?")
        ans6 = input("A. Hurricane\nB. Make You Feel My Love\nC. Lay, Lady, Lay\n").strip()
        if ans6.upper() == "B":
            print("Correct!\n")
            score += 1
            break
        elif ans1.upper() == "C" or ans1.upper() == "A":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

    # final score
    print("You scored" + " " + str(score) + " " + "out of 10!\n")

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
