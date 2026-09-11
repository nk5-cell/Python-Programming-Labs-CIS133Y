#this is an output function
def outputDisplayCalc(inputValue2, letterGrade, name):
    print("Enter 1, 2, 3, 4, 5 for the following options: ")
    print("1. display class roster")
    print("2. display total number of students in class")
    print("3. display number of students per letter grade")
    print("4. display the percentage of each letter grade")
    print("5. exit this program")
    #validates input
    try:
        # input the options to display the outputs
        displayInput = int(input("Enter >> "))
        # count each letter grade
        numAGrade = letterGrade.count('A')
        numBGrade = letterGrade.count('B')
        numCGrade = letterGrade.count('C')
        numDGrade = letterGrade.count('D')
        numFGrade = letterGrade.count('F')
        if displayInput == 1:
            #display student name and their grades
            for studentNames in name:
                print("Roster of your Class: \n---------------------")
                for grades in letterGrade:
                    print("Student Name: " + str(studentNames) + " | Letter Grade: " + str(grades))
        elif displayInput == 2:
            print("There are total of " + str(len(name)) + " students in the system")
        elif displayInput == 3:
            #display number of A's B's C's D's F's
            print("Number of students that got 'A' are: " + str(numAGrade))
            print("Number of students that got 'B' are: " + str(numBGrade))
            print("Number of students that got 'C' are: " + str(numCGrade))
            print("Number of students that got 'D' are: " + str(numDGrade))
            print("Number of students that got 'F' are: " + str(numFGrade))
        elif displayInput == 4:
            #Display the percentage of each letter grade
            print("Letter Grade [A, B, C, D, F) in your class: ")
            #calculations: takes the number of A's B's C's D's F's and
            # divides it by total number of letter grades in the system, and
            # then multipy it by 100 to display the percentage
            print(f"{(numAGrade/len(letterGrade))*100:.2f}% students got A's")
            print(f"{(numBGrade/len(letterGrade))*100:.2f}% students got B's")
            print(f"{(numCGrade/len(letterGrade))*100:.2f}% students got C's")
            print(f"{(numDGrade/len(letterGrade))*100:.2f}% students got D's")
            print(f"{(numFGrade/len(letterGrade))*100:.2f}% students got F's")
        elif displayInput == 5:
            print("Good Bye!!!")
    except ValueError:
        print("Invalid input, please enter again.")
        #calls this same outputDisplayCalc() function
        outputDisplayCalc(inputValue2, letterGrade, name)

