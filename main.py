#*****************************************************************************
#Author:            Nidhi Kairon
#Description:       This is a program for instructors to track students
#                   performance
#Input:             inputValue, studentName, studentLetterGrade, exitingSystem,
#                   displayInput, which outputs their roster, total number of
#                   students, number of students per letter grade, and
#                   percentage of each letter grade
#Output:            numAGrade, numBGrade, numCGrade, numDGrade, numFGrade,
#                   studentNames, grades,
#*****************************************************************************

import inputs
import outputs

def main():
    name = []
    letterGrade = []
    inputValue2 = 0
    inputsFunction = inputs.inputsFunction(letterGrade, name)
    outputDisplayCalc = outputs.outputDisplayCalc(inputValue2, letterGrade, name)
    print(inputsFunction)
    print(outputDisplayCalc)

main()
