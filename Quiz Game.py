print("Welcome to the quiz game.")
answer= input("Are you ready to play it? :")
score = 0 
totalquestion= 10

while answer.lower() == "yes" or answer.lower() == "y":
    answer = input("1. What is the capital of UAE?  t  The options are :\n A Dubai\n B Abu Dhabi \n C Ajman \n D Fujarah \n ")
    if answer.lower() == "abu dhabi" or answer.lower() == "b":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print("")
    answer = input("2. Unjumble the words and find the correct company brand name. The letters are : RACE ")
    if answer.lower() == "acer":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    answer = input("3.Which is the most famous coding language? ")
    if answer.lower() == "python":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    answer = input(" 4.What is the population of India? (As per 2025 stats) ")
    if answer.lower() == "1.4 bilion"  or answer.lower() == "1.4bilion": 
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    answer = input("5.Do we fill normal air inside the tyres of the aircraft? ")
    if answer.lower() == "no":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    answer = input("6. In which aircraft model is the MCAS system fited? ")
    if answer.lower() == "737 max family":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    answer = input("7. What is the most latest fighter jet Lockheed has created? ")
    if answer.lower() == "f35"  or answer.lower() == "f 35":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    answer = input("8.When was the last flight the Concorde took? (Please mention the date) ")
    if answer.lower() == "24 october 2003" or answer.lower() == "24/10/2003" or answer.lower() == "24-10-2003" or answer.lower() == "10/24/2003" or answer.lower() == "24 oct 2003":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    answer = input("9.What is the full form of FAA ? ")
    if answer.lower() == "fedral aviation administration":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    answer = input("10.Who is the chinese aircraft maufacturers? ")
    if answer.lower() == "comda":
        score = score + 1
        print("The answer is correct!")
    else:
        print("Incorrect answer.")
    print()

    print("Thank you for playing. Your total right answers were", score)
    percentage = (score/totalquestion)*100
    print("Your percentage is ", percentage)
    if percentage > 80:
     print("Very good you were excellent in answering the questions. ")
    elif percentage > 60 and percentage <= 80:
     print("You did well try to make it better. ")
    else:
      print("You did terrible.")
    answer  = input("Do you wish to redo the quiz game? ")
else:
 print("Thank you for playing the quiz game.")
 breakpoint