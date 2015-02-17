__author__ = 'Charles C. Lee'

answers = "ddbcdded"

for number, answer in enumerate(list(answers)):
    print("{}. {}".format(number+1, answer.upper()))

# Lab 3

def quiz():

    total_correct = 0


    def correct_response(total_correct):
        print("That's correct")
        return total_correct + 1

    def incorrect_response():
        print("That's not correct.")

    print("Quiz Time!\n")
    question_1 = input("How many books are there in the Harry Potter series? >>> ")
    if question_1 in "7seven":
        total_correct = correct_response(total_correct)
    else:
        incorrect_response()
    question_2 = int(input("What is 3*(2-1)? >>> "))
    if question_2 == 3:
        total_correct = correct_response(total_correct)
    else:
        incorrect_response()

    question_3 = int(input("What is 3*2-1? >>> "))
    if question_3 == 5:
        total_correct = correct_response(total_correct)
    else:
        incorrect_response()

    print("Who sings Black Horse and the Cherry Tree?")
    print("1. Kelly Clarkson")
    print("2. K.T. Tunstall")
    print("3. Hillary Duff")
    print("4. Bon Jovi")
    question_4 = int(input("Your answer >>> "))
    if question_4 == 2:
        total_correct = correct_response(total_correct)
    else:
        incorrect_response()

    print("Who is on the front of a one dollar bill?")
    print("1. George Washington")
    print("2. Abe Lincoln")
    print("3. John Adams")
    print("4. Thomas Jefferson")
    question_5 = int(input("Your answer >>> "))
    if question_5 == 1:
        total_correct = correct_response(total_correct)
    else:
        incorrect_response()

    print("Congratulations you got {} answers correct.".format(total_correct))
    print("That is a score of %{}. ".format(total_correct/5*100))

quiz()
