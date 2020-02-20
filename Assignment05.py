# ------------------------------------------------------------------------ #
# Title: Assignment05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# ASimpson, 02/17/2020.  Created a script of "To Do" List tasks. Print Tasks to
# a table, Add a new task, remove a task, save data to text file and exit.
# Also, added code to complete assignment 5.  Used Separation of Concerns (SoC) to
# divide the code into the Data, Processing and I/O sections.
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
# objFile = "ToDoList.txt"   # An object that represents a file path
strFile = "C:\\_PythonClass\\Assignment05\\ToDoList.txt"
# A file object opened here using the above path
objFile = open(strFile, "r")
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
# This Task ID Integer variable is needed to reset my Task IDs
intTaskID = 0
# This boolean value will help me with figuring out when to reset my IDs
flgUpdateIDs = False
# This boolean value variable will help me with figuring out if the Task name exists or not
flgTaskFound = False

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# Open the "ToDoList" text file and read lines into memory
# Use a for loop to build a table of dictionaries
for row in objFile:
    # For each row in the file split values by looking for the ","
    lstRow = row.split(",")
    # Create a dictionary of values in this statement
    dicRow = {"ID": lstRow[0], "Task": lstRow[1], "Priority": lstRow[2].strip()}
    # Append the dictionary to the table
    lstTable.append(dicRow)
# Close the file object after data is read into memory
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
     Menu of Options
     1) Show current To Do List.
     2) Add a new Task to the List.
     3) Remove an existing Task.
     4) Save Data to File
     5) Exit Program
     """)
    # Setup the user input and give instructions
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        # Added this print statement for a line return, formatting and readability
        print()
        # Added the following 3 print statements to build the table of task items
        print("     ++++++++++++++++++++++++++++++++++++++")
        print("      |  ID:  |   Task:         |  Priority:  ")
        print("     --------------------------------------")
        # Added a For Loop here to run through each of the rows in the table and then print them in the table
        for item in lstTable:
            # Using a print statement here to organize the items in the table,
            print("    ", item.get("ID"), item.get("Task"), item.get("Priority"), sep="   |  ")
            # Added this print statement for formatting and readability
            print("     --------------------------------------")
        # Added this print statement for formatting and readability
        print("")
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        while True:
            # Get the User input about the new task
            NewTask = input("What's the New Task Name?:  ")
            # See if the New Task Name is already in the table, if not add it to the table
            for item in lstTable:
                if NewTask == item.get("Task"):
                    # if we find the Task Name set this flag to True
                    flgTaskFound = True
                    # Let the user know that the given task name already exists using this print statement
                    print("The given task name already exists.  Enter another task name.")
                    break
            # Evaluate if the script found the task name t/f.  If False, Ask the user about priority
            if not flgTaskFound:
                # Get the User input about the task priority
                TaskPriority = input("What's the priority of this task?: ")
                # Get the length of the Table so that we know which item ID number is next
                intTaskID = len(lstTable)
                # Increment the item ID by 1
                intTaskID += 1
                # Create the dictionary row object using the user input values and the next ID value
                dicRow = {"ID": intTaskID, "Task": NewTask, "Priority": TaskPriority}
                # Append the dictionary row to the List Table
                lstTable.append(dicRow)
                flgTaskFound = False
                # Collect the user's choice to add another Task
                strUserSaveChoice = input("Add another Task? (y/n):  ")
                # Evaluate the users choice here, if "n" than exit loop
                if strUserSaveChoice.lower() == "n":
                    # Set this flag to False if the user enters "n"
                    flgTaskFound = False
                    # Exit the loop and go to the Main Menu
                    break
            # Set this Task Found value to false to reset the while loop and try again
            flgTaskFound = False
    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        while True:
            # Get user input about which task to remove from the list
            ExistingTask = input("Remove a Task from the list?:  ")
            # Use a for loop to go through each of the dictionaries in the table
            for objRow in lstTable:
                # Compare the user given task name with the values in each dictionary
                if ExistingTask in objRow.values():
                    # Let the user know that the task name is valid and will be removed
                    print("Removing this task from the list: " + ExistingTask)
                    # Remove the Task Name form the ToDoList
                    lstTable.remove(objRow)
                    # Set a flag here to true so that I can re-order the item IDs properly
                    flgUpdateIDs = True
            # Check to see if the item IDs need to be reset, if True then cycle through each row
            if flgUpdateIDs is True:
                # Set the task ID to zero here
                intTaskID = 0
                # Use a for loop to update each dictionary row in the list table
                for objRow in lstTable:
                    # Increment the Task ID value by 1
                    intTaskID += 1
                    # Update the "ID" value in each dictionary row
                    objRow.update({"ID": str(intTaskID)})
                # Set the Flag Update to False here so that it's in the
                # right position for the next time through the code
                flgUpdateIDs = False
            elif flgUpdateIDs is False:
                print("Could not find the Task Name provided.")
            # Collect the user's choice to add another Task
            strUserSaveChoice = input("Try Removing Another Task Name? (y/n):  ")
            # Evaluate the users choice here, if "n" than exit loop
            if strUserSaveChoice.lower() == "n":
                # Set this Flag to False if user answers "n"
                flgUpdateIDs = False
                # Go back to Main Menu
                break
    # Step 6 - Save the Data or Task List to the text file
    elif strChoice.strip() == '4':
        # Added this print statement for a line return, formatting and readability
        print("")
        # Use a print statement to send save choice instructions to the user
        print(" Would you like to save your current task list?")
        # Collect the user's choice to save or no save here
        strUserSaveChoice = input(" Enter 'y' or 'n': ")
        # Evaluate the users choice here, if "y" than yes, write the data to a text file
        if strUserSaveChoice.lower() == "y":
            # Use a For Loop to write each table row or item to a text file here
            objFile = open(strFile, "w")
            for item in lstTable:
                # write the name of the item and the value to the Home Inventory List text file
                objFile.write(
                    str(item.get("ID")) + "," + str(item.get("Task")) + "," + str(item.get("Priority")) + "\n")
            # Send a message to the user notifying them that the input has been saved
            print(" Task List Saved!!")
            # Close the text file object here
            objFile.close()
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        # Exit the While Loop with the break command
        break  # and Exit the program
    else:
        # Use a print statement to send a reminder to the user
        print(' Please choose only 1, 2, 3, 4 or 5!!!!"')
# Send a nice message to the end user, close file object and exit program
print("Now exiting the To Do List program.  Goodbye!")
# Finally, close the text file when user enter "exit" to exit the program
