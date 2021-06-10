# Get input for variables of kinematic equations
# Ask user what they want to solve for
# have different functions to handle different scenarios

from sympy import symbols, solve

possibleVariables = {"final velocity": None, "initial velocity": None, "time": None, "acceleration": None, "displacement": None}
possibleVariablesUnits = {"final velocity": "m/s", "initial velocity": "m/s", "time": "seconds", "acceleration": "m/s^2", "displacement": "meters"}

def main():
    print("Welcome to the Kinematics Calculator!")
    answer = input("What do you want to solve for? final velocity, inital velocity, time, acceleration, displacement\n").lower()
    possibleVariables[answer] = symbols("lookfor")

    for v in possibleVariables:
        if answer.lower() != v.lower():
            prompts(v)

    if possibleVariables["displacement"] == None:
        print("Equation Used: Vf = Vi + at")
        print(answer, "is", equation1(), possibleVariablesUnits[answer])

    elif possibleVariables["final velocity"] == None:
        print("Equation Used: d = Vit + 0.5at^2")
        print(answer, "is", equation2(), possibleVariablesUnits[answer])

    elif possibleVariables["time"] == None:
        print("Equation Used: Vf^2 = Vi^2 + 2ad")
        print(answer, "is", equation3(), possibleVariablesUnits[answer])

    else:
        print("Sorry try again")


def prompts(knownVariable):
    decision = input("Do you have " + knownVariable + "?" + " Type yes if you do\n")
    if decision.lower() == "yes":
        value = float(input("What is it?\n"))
        possibleVariables[knownVariable] = value

def equation1():
    expression1 = possibleVariables["initial velocity"] + possibleVariables["acceleration"] * possibleVariables["time"] - possibleVariables["final velocity"]
    
    finalAnswer = round((solve(expression1)[0]), 3)

    return finalAnswer

def equation2():
    expression2 = possibleVariables["initial velocity"] * possibleVariables["time"] + 0.5 * possibleVariables["acceleration"] * possibleVariables["time"] ** 2 - possibleVariables["displacement"]
    
    possibleFinalAnswers2 = solve(expression2)
    if len(possibleFinalAnswers2) > 1:
        if possibleFinalAnswers2[0] < 0:
            return round(possibleFinalAnswers2[1], 3)

    return round(possibleFinalAnswers2[0], 3)

def equation3():
    expression3 = possibleVariables["initial velocity"] ** 2 + 2 * possibleVariables["acceleration"] * possibleVariables["displacement"] - possibleVariables["final velocity"] ** 2

    finalAnswer3 = round((solve(expression3)[0]), 3)
    
    return finalAnswer3

main()