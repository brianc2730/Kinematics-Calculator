# Get input for variables of kinematic equations
# Ask user what they want to solve for
# have different functions to handle different scenarios

from sympy import symbols, solve

possibleVariables = {"final velocity": None, "initial velocity": None, "time": None, "acceleration": None, "displacement": None}
possibleVariablesUnits = {"final velocity": "m/s", "initial velocity": "m/s", "time": "seconds", "acceleration": "m/s^2", "displacement": "meters"}

def main():
    print("Welcome to the Kinematics Calculator!")
    validSolveFor = False
    while not validSolveFor:
        answer = input("What do you want to solve for? final velocity, inital velocity, time, acceleration, displacement\n").lower()
        if answer not in possibleVariables:
            print("Not a valid variable. Try again.")
        else:
            validSolveFor = True

    possibleVariables[answer] = symbols("lookfor")

    for v in possibleVariables:
        if answer.lower() != v.lower():
            if v.lower() == "acceleration" or v.lower() == "initial velocity":
                while True:
                    try:
                        requiredKnownVariable = float(input("What is the " + v + "?\n"))
                        possibleVariables[v] = requiredKnownVariable
                        break 
                    except ValueError:
                        print("Must have a valid " + v + ". Please type a valid number.")
            else:
                prompts(v)
    while True:
        try:
            if possibleVariables["displacement"] == None:
                print(answer, "is", equation1(), possibleVariablesUnits[answer])
                print("Equation Used: Vf = Vi + at")

            elif possibleVariables["final velocity"] == None:
                print(answer, "is", equation2(), possibleVariablesUnits[answer])
                print("Equation Used: d = Vit + 0.5at^2")

            elif possibleVariables["time"] == None:
                print(answer, "is", equation3(), possibleVariablesUnits[answer])
                print("Equation Used: Vf^2 = Vi^2 + 2ad")
            else:
                print("Sorry, inputted too many values. Try again")
            break
        except TypeError:
            print("Sorry, didn't input enough values. Try again.")
            break

def prompts(knownVariable):
    decision = input("Do you have " + knownVariable + "?" + " Type yes if you do\n")
    if decision.lower() == "yes":
        while True:
            try:
                value = float(input("What is it?\n"))
                possibleVariables[knownVariable] = value
                break
            except ValueError:
                print("Not a number. Please input a valid number")

def equation1():
    expression1 = possibleVariables["initial velocity"] + possibleVariables["acceleration"] * possibleVariables["time"] - possibleVariables["final velocity"]
    
    finalAnswer1 = round((solve(expression1)[0]), 3)

    return '{:.3f}'.format(finalAnswer1)

def equation2():
    expression2 = possibleVariables["initial velocity"] * possibleVariables["time"] + 0.5 * possibleVariables["acceleration"] * possibleVariables["time"] ** 2 - possibleVariables["displacement"]
    
    possibleFinalAnswers2 = solve(expression2)
    if len(possibleFinalAnswers2) > 1:
        if possibleFinalAnswers2[0] < 0:
            return '{:.3f}'.format(round(possibleFinalAnswers2[1], 3))

    return '{:.3f}'.format(round(possibleFinalAnswers2[0], 3))

def equation3():
    expression3 = possibleVariables["initial velocity"] ** 2 + 2 * possibleVariables["acceleration"] * possibleVariables["displacement"] - possibleVariables["final velocity"] ** 2

    if type(possibleVariables["final velocity"]) is not float:
        finalAnswer3 = round((solve(expression3)[1]), 3)
    else:
        finalAnswer3 = round((solve(expression3)[0]), 3)
    
    return '{:.3f}'.format(finalAnswer3)

main()