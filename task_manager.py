
# imports date library, used for current date

import datetime

# stores all lines of text inside program
# this minimises open time for file

lines = []
# all usernames will be stored in this list

all_users = []

# all passwords will be stored in this list

all_pw =    []

# opens user text file in read-only format

with open("user.txt", "r") as f:

    # reads over every line in the text file
    lines = f.readlines()

    
    # for each line in the text
    # the line is split into 2 columns
    # the first column is the username, and the second is their password
    # the username is added to the all_users list
    # the password is added to the all_pw list
    
    for i in range(len(lines)):
        current =       lines[i].split(", ")
        txt_name =      current[0]
        all_users.append(txt_name)
        txt_pw =        current[1]
        all_pw.append(txt_pw.strip("\n"))

# prompts the user to enter their username        

name = input("Please enter your username: ")

# if the username does not appear in the list of registered users, they will be asked to enter one that does appear in the list

while name not in all_users:
    name = input("Please enter a valid username: ")

# prompts the user to enter the password associated with the valid username

password = input("Please enter your password: ")

# checks index of password in all_pw list

pw_index = all_pw.index(password)

# checks if username and password appear at the same index in their respective list
# this would mean they are on the same row, i.e., the same user

correct_password = all_users[pw_index]

# if the password does not match the registerd user, they will be prompted to enter the correct password

while name != correct_password:
    password = input("This password is not valid for this username. Please try again: ")

# if the user logs in as admin, they have administrative access, giving them an additional option in the menu

if name == "admin":

    # menu of options for the user
    
    option = input(
        '''
        Please select one of the following options: 
        r -     register user
        a -     add task
        va -    view all tasks
        vm -    view my tasks
        e -     exit
        s -     display statistics
        '''
        ).lower().strip()

    # these are the valid options
    
    valid = ["r", "a", "va", "vm", "e", "s"]

    # if the user selects an invalid option, they will be prompted to enter a valid input
    
    while option not in valid:
        option = input(
        '''
        Please select one of the following options: 
        r -     register user
        a -     add task
        va -    view all tasks
        vm -    view my tasks
        e -     exit
        s -     display statistics
        '''
        ).lower().strip()

    # admin only option
    # this shows the user details about all tasks in tasks.txt file
    
    if option == 's':
        
        # initialises counts at 0
        
        num_users = 0
        num_tasks = 0

        # reads user.txt file
        # counts number of lines
        # num_users set at number of lines
        
        with open("user.txt", "r") as f:
            lines =     f.readlines()
            num_users = len(lines)
        
        # reads tasks.txt file
        # counts number of lines
        # num_tasks set at number of lines
        
        with open("tasks.txt", "r") as f:
            lines =     f.readlines()
            num_tasks = len(lines)

        # prints out number of users and tasks in a user-friendly format, using fstrings
        
        print(f"Total number of users: {num_users}")
        print(f"Total number of tasks: {num_tasks}")

    # allows registration of new users

    elif option == "r":

        # prompts user to enter a username and password for the new user
        # asks user to confirm password

        new_user =      input("Please enter a new username: ")
        new_pw =        input("Please enter a new password: ")
        confirm_pw =    input("Please confirm password: ")

        # if the user already exists, it will prompt for a username that does not already exist

        while new_user in all_users:
            new_user = input("This user already exists. Please enter a new username: ")
        
        # check that the confirmed password is the same

        if confirm_pw == new_pw:

            # adds new user to user.txt file in the correct format

            fuser = "\n{}, {}".format(new_user, new_pw)
            with open("user.txt", "a") as f:
                f.write(fuser)
            
            # alerts user that registration was successful

            print("Registration successful!")


# displays options for non-admin users
# all valid answers stored in a list "valid"
# option menu for users represented as a multiline string
# formats options to eliminate differences in case, as well as spaces before and after
# if input from user is not valid, the menu will pop uo unitl a valid input is entered

else:
    valid = ["a", "va", "vm", "e"]

    option = input(
    '''
    Please select one of the following options: 
    a -     add task
    va -    view all tasks
    vm -    view my tasks
    e -     exit
    '''
    ).lower().strip()

    while option not in valid:
        option = input(
        '''
        Please select one of the following options: 
        a -     add task
        va -    view all tasks
        vm -    view my tasks
        e -     exit
        '''
        ).lower().strip()

# if user enters "a" it will ask the user a host of questions
# these questions are: users' username, name of the task, name of the task, description of the task, due date, assigned date and whether the task is completed ot not
# assgined date is initialized to the current date 
# import datetime function in line 2 is used to set the format of the date in the variable "fassigned_date"
# all the inputs are stored in a format string variable "new_task"
# "task.txt" file is opened in the append mode and the "new_task" variable with all the users input is then stored in the file

if option == 'a':
     
    print("Please enter the following: ")
    user =          input(
        "username: "
    )
    title =         input(
        "name of task: "
    )
    desc =          input(
        "description of task: "
    )
    due_date =      input(
        "due date of task (eg. 01 Sep 2021): "
    )
    assigned_date = datetime.datetime.now()
    completed =     "No" 

    fassigned_date = assigned_date.strftime(
        "%d %b %Y"
    ) 

    new_task = "{}, {}, {}, {}, {}, {}".format(user, title, desc, due_date, fassigned_date, completed)

    with open("tasks.txt", "a") as f:
        f.write("\n{}".format(new_task))
        
# if user selects "va" the "tasks.txt" file is then opened in read only mode
# empty list is created named "all_tasks"
# for loop that iterates through every item in the list
# "all_tasks" list appended with the current variable

elif option == 'va':
    all_tasks = []
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            current = lines[i]
            all_tasks.append(current)
        
    # empty list created to hold different details of each task

    split_tasks = []

    # each task is split to separate its details
    # details for each task appended to split_tasks list

    for i in all_tasks:
        ftasks = i.strip("\n").split(", ")
        split_tasks.append(ftasks)

    # for each individual task, the details are saved to their own variables

    for i in range(len(split_tasks)):
        assigned =          split_tasks[i][0]
        task =              split_tasks[i][1]
        description =       split_tasks[i][2]
        date_assigned =     split_tasks[i][3]
        due_date =          split_tasks[i][4]
        task_complete =     split_tasks[i][5]

        # single_ftask is a formatted string holding the details of a task in a user friendly format

        single_ftask = '''
        __________________________________________________

        Task:               {}
        Assigned to:        {}
        Date assigned:      {}
        Due date:           {}
        Task Complete?      {}
        Task description:   {}
        __________________________________________________

        '''.format(task, assigned, date_assigned, due_date, task_complete, description)

        # each formatted individual task is presented to the user
        
        print(single_ftask)

# displays only the tasks assigned to the user who is signed in 
# functionally identical to "view all" (line 234 to 280), but one major difference (see line 321)

elif option == 'vm':
    all_tasks = []
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            current = lines[i]
            all_tasks.append(current)
        f.close()

    # empty list created to hold different details of each task

    split_tasks = []

    # each task is split to separate its details
    # details for each task appended to split_tasks list

    for i in all_tasks:
        ftasks = i.strip("\n").split(", ")
        split_tasks.append(ftasks)

    # for each individual task, the details are saved to their own variables

    for i in range(len(split_tasks)):
        assigned =          split_tasks[i][0]
        task =              split_tasks[i][1]
        description =       split_tasks[i][2]
        date_assigned =     split_tasks[i][3]
        due_date =          split_tasks[i][4]
        task_complete =     split_tasks[i][5]

        single_ftask = '''
        __________________________________________________
        
        Task:               {}
        Assigned to:        {}
        Date assigned:      {}
        Due date:           {}
        Task Complete?      {}
        Task description:   {}
        __________________________________________________

        '''.format(task, assigned, date_assigned, due_date, task_complete, description)

        # only prints a task if the assigned user matches the signed in user

        if assigned == name:
            print(single_ftask)

# if user enters "e" it exits the program and a thank you message is dispalyed

elif option == 'e':
    print("Thank you, have a nice day!")