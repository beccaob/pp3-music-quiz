def play_quiz():
    """
    quiz game - if player guesses
    correctly, score goes up by one
    """
    score = 0

# Q1
    while True:
        print("Which symbol was the title of Ed Sheerans first album?")
        ans1 = input("A. +\nB. =\nC. %\nj").strip()
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
        elif ans2.upper() == "A" or ans2.upper() == "C":
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
        elif ans3.upper() == "B" or ans3.upper() == "C":
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
        elif ans4.upper() == "B" or ans4.upper() == "A":
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
        elif ans5.upper() == "C" or ans5.upper() == "A":
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
        elif ans6.upper() == "C" or ans6.upper() == "A":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q7
    while True:
        print("Which prison did Johnny Cash famously sing about in his 1955 song?")
        ans7 = input("A. Folsom\nB. Alcatraz\nC. Ohio State\n").strip()
        if ans7.upper() == "A":
            print("Correct!\n")
            score += 1
            break
        elif ans7.upper() == "C" or ans7.upper() == "B":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q8
    while True:
        print("What was the name of the band formed by Jack Bruce, Eric Clapton, and Ginger Baker?")
        ans8 = input("A. Cream\nB. Doobie Brothers\nC. ACDC\n").strip()
        if ans8.upper() == "A":
            print("Correct!\n")
            score += 1
            break
        elif ans8.upper() == "C" or ans8.upper() == "B":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q9
    while True:
        print("Who originally recorded the classic ballad I Will Always Love You in 1973?")
        ans9 = input("A. David Bowie\nB. Dolly Parton\nC. Whitney Houston\n").strip()
        if ans9.upper() == "B":
            print("Correct!\n")
            score += 1
            break
        elif ans9.upper() == "C" or ans9.upper() == "A":
            print("Oops! That's incorrect.\n")
            break
        else:
            print("Invalid answer! Please choose between A, B or C\n")

# Q10
    while True:
        print("Which band had a huge international hit album in 2002 with the record "A Rush of Blood to the Head"?")
        ans10 = input("A. Bowling For Soup\nB. My Chemical Romance\nC. Coldplay\n").strip()
        if ans10.upper() == "C":
            print("Correct!\n")
            score += 1
            break
        elif ans10.upper() == "B" or ans10.upper() == "A":
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
