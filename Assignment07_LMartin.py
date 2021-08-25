# ----------------------------------------------------#
# Title: Assignment 07 - Yule Gifts
# Description: A file that serves as a Yule gift list for people.
#       This script must utilize:
#           1) Exception Handling
#           2) Pickling
# Dev: LMartin
# Date Created: 8/19/2021
# Change Log: (Who, When, What)
# LMartin - 8/19/2021 | Created Menu, Variables, Adding Gifts
# LMartin - 8/23/2021 | Continued Working on Menu Options
# LMartin - 8/24/2021 | Finished Menu Options and added Pickling/Exception Handling
# ----------------------------------------------------#

# Declared Variables ---------------------------------#
objFile = "YuleGifts.txt"   # Text file containing Yule Gift data
objPickleFile = "YuleGifts.dat" # Pickled file containing Yule Gift data
strGift = "" # Yule Gift Idea
strRecipient = "" # Recipient of Gift
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
lstYuleGift = [] # A list of pickled data that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection

# Processing -----------------------------------------#

# Read Data from existing file when the program starts.
try:
    objFile = open("YuleGifts.txt", "r")
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Recipient": lstRow[0], "Gift": lstRow[1].strip()}
        lstTable.append(dicRow)
except IOError:
    print("ERROR - Cannot locate data file.")
else:
    print("Data successfully loaded.")
    objFile.close()

# Input/Output ---------------------------------------#

# Display Menu
while (True):
    print("""
    ~~~ Yule Gift Ideas Menu ~~~
    1) Display Current Gift List
    2) Add Gifts to List
    3) Remove a Gift from the Yule List
    4) Save Yule List to Text File
    5) Pickle Data
    6) View Pickled Data
    7) Exit Program
    """)
    strChoice = str(input("Which option would you like to do? [1 to 7] - "))
    print()  # adding a new line for looks

# Display Current Gift List
    if (strChoice.strip() == "1"):
        print("~~~ Current Yule Gift List ~~~")
        for objRow in lstTable:
            print("| ", objRow["Recipient"], " | ", objRow["Gift"], " |", sep="")
        continue

# Adding New Gift
    elif (strChoice.strip() == "2"):
        print("\nType in a recipient and gift for the Yule Gift List.")
        try:
            strRecipient = str(input("\nRecipient: "))
            strGift = str(input("Gift: ")).strip()
        except strGift == "coal":
            print("ERROR - That's not very nice! Enter in a proper gift.")
        finally:
            dicRow = {"Recipient": strRecipient, "Gift": strGift}
            lstTable.append(dicRow)
            print("\nThe Recipient -|" + strRecipient + "|- and Gift -|" + strGift + "|- have been added.")
        continue

# Remove a Gift from the Yule List
    elif (strChoice.strip() == "3"):
        while(True):
            print("Which gift do you want to remove from the Yule List? OR type 'exit' to return to the menu."
                  "\nFYI - Please use lower case font. ")
            strGift = input("Gift: ")
            if strGift.lower() == "exit":
                break
            for row in lstTable:
                if row ["Gift"].lower() == strGift.lower():
                    lstTable.remove(row)
                    print("SUCCESS - Gift has been removed.")
                    print(lstTable)
                    break
            else:
                print("ERROR - Gift not found.")
                print(lstTable)
                strChoice = input("Exit? Yes (y) or No (n): ")
                if strChoice.lower() == "y":
                    break
                elif strChoice.lower() == "n":
                    break
                else:
                    print("ERROR - Invalid Input.")
                break
        continue

# Save Yule List to Text File
    elif (strChoice.strip() == "4"):
        objFile = open("YuleGifts.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Recipient"]) + "," + str(row["Gift"]) + "\n")
        objFile.close()
        print("SUCCESS - Yule List has been saved.")
        continue

# Pickle Data
    elif (strChoice.strip() == "5"):
        import pickle
        objFile = open("YuleGifts.dat", "wb")
        pickle.dump(lstTable, objFile)
        objFile.close()
        print("SUCCESS - Yule List has been pickled!")
        continue

# View Pickled Data
    elif (strChoice.strip() == "6"):
        objPickleFile = open("YuleGifts.dat", "rb")
        objFileData = pickle.load(objPickleFile)
        print(objFileData)
        objFile.close()
        continue

# Exit Yule List Program
    elif (strChoice.strip() == "7"):
        EndProgram = input("(Press Enter to exit.)")
        break  # and Exit the program