import math, sys, os, re

def clear():
    os.system("cls")

# SIMPLE ARITHMETICS
def main():
    clear()
    print("\nYou chose Simple Arithmetics!")
    while True:
        userInput = input("\nPlease enter two numbers and the operator you wish to use, eg 2 + 2 \n = ")
        userInputList = re.split("\s", userInput)

        try:
            # ADDITION
            if userInputList[1] == "+":
                # PI
                if userInputList[0] == "pi":
                    userInputList[0] = 3.141592653589793
                elif userInputList[2] == "pi":
                    userInputList[2] = 3.141592653589793
                ans = float(userInputList[0]) + float(userInputList[2])
                print("\nThe answer is =", + ans)
                break

            # SUBTRACTION
            if userInputList[1] == "-":
                # PI
                if userInputList[0] == "pi":
                    userInputList[0] = 3.141592653589793
                elif userInputList[2] == "pi":
                    userInputList[2] = 3.141592653589793
                ans = float(userInputList[0]) - float(userInputList[2])
                print("\nThe answer is =", + ans)
                break

            # MULTIPLICATION
            if userInputList[1] == "*":
                # PI
                if userInputList[0] == "pi":
                    userInputList[0] = 3.141592653589793
                elif userInputList[2] == "pi":
                    userInputList[2] = 3.141592653589793
                ans = float(userInputList[0]) * float(userInputList[2])
                print("\nThe answer is =", + ans)
                break

            # DIVISION
            if userInputList[1] == "/":
                # PI
                if userInputList[0] == "pi":
                    userInputList[0] = 3.141592653589793
                elif userInputList[2] == "pi":
                    userInputList[2] = 3.141592653589793
                ans = float(userInputList[0]) / float(userInputList[2])
                print("\nThe answer is =", + ans)
                break

        except IndexError:
            print("\nERROR : Please add a space between numbers")
            continue


# COMPLEX ARITHMETICS
def complexArithmetics():
    clear()
    print("-\nYou chose Complex Arithmetics!")
    while True:
        userInput = input("-\nPlease enter two numbers and the operator you wish to use, eg 2 ^ 3 \n= ")
        userInputList = re.split("/", userInput)
        # SQUARED ROOT
        if "square" in userInputList:
            ans = math.sqrt(float(userInputList[1]))
            print("-\nThe answer is =", + ans)
            break
        else:
            # EXPONENTS
            userInputList = re.split("\s", userInput)
            if userInputList[1] == "^":
                ans = float(userInputList[0]) ** float(userInputList[2])
                print("-\nThe answer is =", + ans)
                break
            else:
                print("ERROR : Please Enter a valid string")



# TRIGONOMETRY
def trig():
    clear()
    print("-\nYou chose Trigonometry!")
    while True:
        userInput = input("-\nPlease enter the problem you wish to solve, eg sin 60 \n= ")
        userInputList = re.split("\s", userInput)
        # SINE
        if "sin" in userInputList:
            ans = math.sin(float(userInputList[1]))
            print("-\nThe answer is = ", + ans)
            break
        # COSINE
        elif "cos" in userInputList:
            ans = math.cos(float(userInputList[1]))
            print("-\nThe answer is = ", + ans)
            break
        # TANGENT
        elif "tan" in userInputList:
            ans = math.tan(float(userInputList[1]))
            print("-\nThe answer is = ", + ans)
            break

        # HYPERBOLICS

        # SINH
        elif "sinh" in userInputList:
            ans = math.sinh(float(userInputList[1]))
            print("-\nThe answer is = ", + ans)
            break
        # COSH
        elif "sinh" in userInputList:
            ans = math.cosh(float(userInputList[1]))
            print("-\nThe answer is = ", + ans)
            break
        # TANH
        elif "sinh" in userInputList:
            ans = math.tanh(float(userInputList[1]))
            print("-\nThe answer is = ", + ans)
            break




# START OF THE PROGRAM
print(
    """\nWelcome to Daniel's scientific text-based calculator!
    -\nFor the manual, Enter 'M'
    -\nTo quit, enter 'q'
    - """)
answer = input()


# NAVIGATES THE USER TO THE DESIRED FUNCTION
while True:

    if answer.lower() == "q":
        clear()
        print("\nBye!")
        sys.exit()

    elif answer.title() == "M":
        # IMPORTS THE MANUAL
        import NewCalculatorProjectManual

        answer3 = input(" = ")

        if answer3.title() == "C":
            main()
            break

        elif answer3.upper() == "CO":
            complexArithmetics()
            break

        elif answer3.upper() == "TRIG":
            trig()
            break

        else:
            answer = input("\nPlease enter a valid string = ")
            continue

    elif answer.upper() == "C":
        main()
        break

    elif answer.upper() == "CO":
        complexArithmetics()
        break

    elif answer.upper() == "TRIG":
        trig()
        break

    else:
        answer = input("\nPlease enter a valid string = ")
        continue


