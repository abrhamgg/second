name = input(" welcome user, Enter your name? \n ")
start = input("hello " + name + ",\n"
                                "please briefly read the following scenarios and\n"
                                "press B to continue\n"
                                "press N to exit \n"
                                "\n"
                                "INSTRUCTION: You have two chances to answer each questions correctly\n"
                                "Seven persons live in a street, having houses in line \n"
                                "1. A lives in the corner house \n"
                                "2. C is between E and G \n"
                                "3. There is 1 house between D and F \n"
                                "4. F is neighbour of G \n"
                                "5. There are two houses between A and G \n "
                                "\n"
                                "the possible arrangement for the houses are \n"
                                "1st  :- A \n"
                                "2nd  :- E, Because in scenario 5 we are declaring that  there are two houses \n"
                                "between A & G and C is between E AND G \n"
                                "3rd  :- C \n"
                                "4th  :- G \n"
                                "5th  :- F \n"
                                "6th  :- B \n"
                                "7th  :- D \n")
if start == "N" or start == "n":
    print("Thank you, GOOD BYE")
    exit()
elif start != "N" and start != "n" and start != "B" and start != "b":
    print("Invalid input, GOOD BYE")

elif start == "B" or start == "b":
    count = 0
    chances = 2
    while count < chances:
        first = input("who lives in the second corner? \n")
        if first != "D" and first != "d":
            print("you are wrong.")
            count = count + 1
        elif first == "d" or first == "D":
            print("you are correct")
            count = chances
    count = 0
    chances = 2
    while count < chances:
        first = input("who lives in the middle? \n")
        if first != "G" and first != "g":
            print("you are wrong.")
            count = count + 1
        elif first == "g" or first == "G":
            print("you are correct")
            count = chances
    count = 0
    chances = 2
    while count < chances:
        first = input("enter the person who live between B and G\n")
        if first != "F" and first != "f":
            print("you are wrong.")
            count = count + 1
        elif first == "f" or first == "F":
            print("you are correct")
            count = chances
    count = 0
    chances = 2
    while count < chances:
        first = input("who is the neighbour of A\n")
        if first != "E" and first != "e":
            print("you are wrong.")
            count = count + 1
        elif first == "E" or first == "e":
            print("you are correct")
            count = chances
    count = 0
    chances = 2
    while count < chances:
        first = input("how many houses are between A and G\n")
        if first != "3":
            print("you are wrong, GOOD BYE")
            count = count + 1
        elif first == "3":
            print("excellent work " + name + ",")
            count = chances
