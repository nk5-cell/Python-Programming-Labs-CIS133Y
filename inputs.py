
#Functon that inputs the students name and their grade
def inputsFunction(letterGrade, name):
    continued = True
    i = 0
    inputValue2 = 0
    #input student name and their grade
    while (continued == True):
        #validates input
        try:
            # prompt the number of student user want to enter in the system
            inputValue = int(input("Enter the amount of student info you want to enter in the system: "))
            inputValue2 += inputValue
            #input student name and their grade
            while i < inputValue2:
                #input student names
                studentName = str(input("Enter student name: "))
                #add students name to the list
                name.insert(i, studentName)

                #student grade input
                studentLetterGrade = input("Enter student letter grade: ").upper()
                #student's grade input validation
                while (studentLetterGrade != 'A' and studentLetterGrade != 'B' and studentLetterGrade != 'C' and studentLetterGrade != 'D' and studentLetterGrade != 'F'):
                    print("Invalid input, please enter again.")
                    studentLetterGrade = input("Enter student letter grade again: ").upper()
                #adds grades to the list
                letterGrade.insert(i, studentLetterGrade)
                #update i
                i+=1
        except ValueError:
            print("Invalid input, please enter again.")
            inputsFunction(letterGrade, name)
        # prompt to exit the loop
        exitingSystem = input('Press q to stop entering more students \nor any key to enter more students: ').lower()
        if exitingSystem == 'q':
            continued = False
    return inputValue2, letterGrade, name
