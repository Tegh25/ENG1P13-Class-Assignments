#!/usr/bin/env python
# coding: utf-8

# # Computing 5 Assignment
# 
# 

# ---
# ## Background
# 
# In this assignment you will be implementing a set of functions used in conjunction to form a website login system. Your system will utilize a text file for storing, retrieving, and verifying user credentials. We identify users based on their **username** and **password**. For simplicity we assume that usernames and passwords only contain alphanumeric characters. Alphanumeric characters represent the numbers **0-9** and the letters **A-Z** (both uppercase and lowercase). Usernames and passwords are case sensitive and must contain **at least 6** characters. Usernames must be unique.
# 
# Each username and password combination will be stored on its own line in the text file. Each line in the text file has the following format:
# 
# 
# <br>
# \begin{align}
#   \texttt{username\tpassword\n}\tag{1}
# \end{align}
# <br>
# 
# More explicitly, each line in the text file will contain a user’s username, a tab character, and that user’s password followed by the newline character. Please note that when opening the text file for viewing you will not explicitly see the **\t** and **\n** characters.
# 
# 
# In your implementation, usernames and passwords will be stored as plain text. This means that all usernames and passwords can easily be compromised if access to the text file is provided. This is extremely dangerous in the real world and poses huge security issues. In practicality, passwords are encrypted before stored so that they are not easily identifiable in the event of a data breach. Thus, please do not use any real passwords when developing and testing your program. 
# 

# ---
# ## Program Requirements (12 Marks)
# 
# Your task is to implement a set of functions that will be used in conjunction to form a website login system. Your system will read and write user credentials from a text file that emulates a database. The requirements of the system are given below. 
# Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks. You can choose to copy and paste the function names into the implementation cell to avoid spelling mistakes.
# 
# 
# 1. Define a function **get_user_data**(*filename*):
#   - ***filename***: A *string* representing the name of the text file (ex. “database.txt”) that stores user login credentials in the form of ```username\tpassword\n```.
#   - **Function Description**: The function performs the following actions as defined by the pseudocode below:
#     - Opens a file with the name *filename* for reading.
#     - Initializes two empty lists: **usernames**, and **passwords**
#     - For each line in file:
#         - Strips the line of the newline character "\n" using strip() and then splits it at the tab "\t" character using split(). 
#         - Extracts the username and password in each line. 
#         - The username is appended as a string to **usernames** and the password is appended as a string to **passwords**. 
#     - Closes the file with the name *filename*<br>*(Note that it is assumed that the file associated with filename exists before the function is called)*    
#   - **Return**: A *list of lists* of length 2 where the first list is the **usernames** list and the second list is the **passwords** list populated with the data from *filename* as described above. <br>
# 
# 
# 2. Define a function **exists**(*username*, *username_list*):
#   - ***username***: A *string* representing a username.
#   - ***username_list***: A *list* containing all usernames from *filename*.
#   - **Return**: *True* if *username* exists in *username_list*, otherwise *False*.<br>*(Hint: Use the **in** keyword.)*
# 
# 
# 3. Define a function **create_user**(*username*, *password*, *username_list*, *filename*):
#   - ***username***: A *string* representing a username.
#   - ***password***: A *string* representing a password.
#   - ***username_list***: A *list* containing all usernames from *filename*.
#   - ***filename***: A *string* representing the name of the text file (ex. “database.txt”) that stores user login credentials in the form of ```username\tpassword\n```.
#   - **Function Description**: The function performs the following actions:
#     - If *username* **does not** exist in *filename*, open *filename* in append mode, write the username and password in the form ```username\tpassword\n```, and close the file.
#     - If *username* **does** exist in *filename*, do nothing.
#   - **Return**: *True* if *username* and *password* were added to *filename*, otherwise *False*<br>*(Hint: Use your **exists** function to check if the username exists in username_list and remember to close your file if you open it.)*
# 
# 
# 4. Define a function **login**(*username*, *password*, *filename*):
#   - ***username***: A *string* representing a username.
#   - ***password***: A *string* representing a password.
#   - ***filename***: A *string* representing the name of the text file
#   - **Function Description**: The function performs the following actions:
#     - If *username* **does** exist in *filename*, find the password associated with *username* in *filename* using the index of the *username* and check if *password* is equal to the expected password.<br> *(Hint: Use your **get_user_data** and **exists** functions and the **index()** method.)*
#     - If the username **does not** exist in *filename*, do nothing.
#   - **Return**: *True* if *password* matches the password associated with *username* in *filename*. *False* if the passwords do not match or *username* does not exist in *filename*.

# ---
# ## Implementation
# Please define all functions in the cell below

# In[13]:


#********************************************
# Write your get_user_data function below: (2.5 marks)
#********************************************

# interacts with database text file to return username/password in easy to use format
def get_user_data(filename):
    file = open(filename)
    # initialize usernames and passwords lists
    usernames = []
    passwords = []
    # iterates through each line of file to extract and append user data to initialized lists
    for line in file:
        line = line.strip("\n")
        line = line.split("\t")
        usernames.append(line[0])
        passwords.append(line[1])
    file.close()
    # all data combined into one nice and tidy list and returned
    user_data = [usernames, passwords]
    return user_data

#********************************************
# Write your exists function below: (2.5 marks)
#********************************************

# verifies if username is present in username_list
# True is exists, otherwise False
def exists(username, username_list):
    return username in username_list

#********************************************
# Write your create_user function below: (2.5 marks)
#********************************************

# adds an entry into user database text file if the same username doesn't already exist
# returns True if entry successful, otherwise returns False
def create_user(username, password, username_list, filename):
    if exists(username, username_list) == False:
        # writes to file in format of username\tpassword\n
        file = open(filename, "a")
        file.write(username + "\t" + password + "\n")
        file.close()
        return True
    else:
        return False

#********************************************
# Write your login function below: (4.5 marks)
#********************************************

# allows user to login if there username and password match
# returns True for successful login, otherwise False
def login(username, password, filename):
    user_data = get_user_data(filename)
    # checks to see if username exists and finds index of username in user_data
    if exists(username, user_data[0]) == True:
        username_index = user_data[0].index(username)
        # checks corresponding index in passwords
        if user_data[1][username_index] == password:
            return True
        else:
            return False
    else:
        return False
        
# Intellectual property of Teghveer Ateliey (atelieyt), all rights reserved 2022 (c).
# Copyright waived if full marks recieved.


# ---
# ## Testing
# 
# The cell below contains a main function that you can use to test your functions. 
# 
# ### Important
# Run the cell where you implemented your functions ***first*** and ensure it outputs with no errors. Then, run the cell below with the main function to verify that your code works correctly with the provided input.
# 

# In[14]:


# TESTING
def main():

    database = "database.txt"
    while True:
        ans = input("Press [q] to quit, [l] to login, [c] to create an account: ")
        if ans == "q":
            # Break if the user quits
            break
        elif ans == "l":
            # Login if the user types in "l"
            uname = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if login(uname, password, database):
                print("Login successful!\n")
            else:
                print("Sorry, login unsuccessful :(\n")
        elif ans == "c":
            # Create an account if the user types in c
            uname = input("Please create a username: ")
            password = input("Please create a password: ")
            # Check if username exists
            username_list = get_user_data(database)[0]
            if create_user(uname, password, username_list, database):
                    print("Account creation successful for user,",uname,"\n")
            else:
                    print("Sorry,",uname,"is already taken!\n")
        else:
            print("Please enter a valid character")
main()


# The main function above utilizes the functions you have created to simulate the login system environment. Inspect the code and play around with the funtionality to test out all of your functions. A file has already been created for you called "database.txt". This file contains one user with the following credentials:
# 
# Username: iLoveMac
# Password: iamthebeststudent123
# 
# Use the credentials to log into the system or create your own using the main function!

# ----------
# ## Code Legibility (6 Marks)
# Your code will be marked on commenting and code legibility.<br>
# The mark breakdown is as follows:<br>
# 
# >- 2 marks for using **appropriate variable names** that indicate what is being stored in that variable<br>
# >- 2 marks for leaving **comments on major parts of your code** such as where you read the file or calculate a summation<br>
# >- 2 marks for **general legibility**. The TA's should be able to understand your code without spending hours reading it. For example do not put your code in one very long line as this is hard for someone else reading your code to understand

# ---
# ## Reflective Questions (6 Marks)
# 
# 1. The **create_user** function requires that filename is opened in append mode in order to add a username/password combinations to filename. What will happen if filename is instead opened in write mode? Assume you are forced to use any access mode other append. Is it possible to re-write the function such that the functionality does not change? Please explain.
# 
# 
# 2. Assume you have to write a function **valid_length** that would check if the *username* and *password* are greater than 6 characters. How would you implement this function?
# 
# 
# 3. Assume you have two functions **encrypt(password)** and **decrypt(encoded_password)**. The function **encrypt** takes a password string and returns an encoded version of the password as a string. The function **decrypt** decodes  the encoded_password string and returns the decoded password as a string. Where would you use these functions in your code if you wanted your login system to store encoded user passwords rather than raw text passwords?
# 
# Please answer all questions in the cell below!

# ```
# DOUBLE CLICK TO EDIT THIS CELL. DO NOT DELETE QUOTATION MARKS
# 
# 1. If filename is opened in write mode, it will erase any prior data in that file and all usernames and passwords will be lost. If we cannot use append mode, we can code our function so that it extracts the data from the file using read mode first. From there, the function can close and reopen the file in write mode and insert the data it obtained from the file in read mode. So yes, it is possible to have a function with the same functionality without append mode.
# 
# 2. the valid_length function would be used in the create_user function where it would be the first line of code after defining create_user. The function valid_length would take the username and password strings and check their length with the len() function. If both strings have a length greater than 6, valid_length will return True, otherwise it will return False. If True, create_user will continue with the rest of its function. If valid_length is False, create_user will do nothing.
# 
# 3. encrypt(password) will be used in the create_user function, where it will encrypt the password before writing it into the database. decrypt(encoded_password) will be used in the login function where it will decrypt the index of the passwords list corresponding to the matching username, and compare the decrypted password to the password inputted by the user.
# 
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 5 dropbox on avenue with the naming convention: macID_CL5.py
# 
# #### NOTE: YOU WILL BE MARKED ON MULTIPLE ITEMS IN THIS LAB IN ADDITION TO THE FUNCTIONALITY OF YOUR CODE
#  - Variable Names
#  - Commenting
#  - General Legibility
#  - Reflective Questions
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely receive zero.**
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST
# 
# Late labs will not be accepted
