#*****************************************************************************
#Author:            Nidhi Kairon
#Description:       This is a program that uses Name data from the US
#                   Census Bureau
#Input:             year, gender
#Output:            name, year, gender, count
#*****************************************************************************

from lab5Name import Name

def main():
    inputval = True
    inputval2 = True
    #input validation
    while inputval == True:
        try:
            year = int(input("Select a year between 1915 and 2014: "))
            if 1915 <= year <= 2014:
                inputval = False
            else:
                print("The year must be between 1915 and 2014!")
        except ValueError:
            print("Please enter a whole number!")
    while inputval2 == True:
        try:
            gender = str(input("Please enter a gender (M/F): ")).upper()
            if gender in ['M', 'F']:
                inputval2 = False
            else:
                print("Please type M or F!")
        except ValueError:
            print("Invalid Input!")

    #calls Name.readNames()
    lstNames = Name.readNames(year, gender)

    #header
    print(f"\n20 most popular name for {gender} babies in {year}:\n")
    print(f"{'Year':<7} {'Name':<20} {'Gender':<10} {'Count'}")

    #loop through each Name object in the list of Name objects
    for n in lstNames:
        print(f"{n.year:<7} {n.name:<22} {n.gender:<8} {n.count}")

if __name__ == "__main__":
    main()
    
    
