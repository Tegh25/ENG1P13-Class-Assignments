#!/usr/bin/env python
# coding: utf-8

# # Computing 6 Assignment
# 
# 

# ---
# ## Background
# 
# In this assignment you will be implementing a portion of a Geographic Information System (GIS). A GIS is a computer system used to organize, categorize, and analyze geographical data in order to produce accurate depiction of the real world. The system uses multiple layers of information to achieve this task. The data layers are split into a grid and represented as a matrix with **m** rows and **n** columns where each entry in the matrix contains the type of land at that point on the map. An entry **A<sub>ij</sub>** is the *i*th row and *j*th column in our map matrix. We assume that **A<sub>00</sub>** is the first element in our matrix. The graphic below will assist in visualizing the process:
# 
# ![Comp6.png](attachment:Comp6.png)
# \begin{align}
#   \texttt{Figure 1}
# \end{align}
# 
# 
# As seen in the previous example, our GIS utilizes **6** different data layers. We call these layers the **map types** as they classify regions of different land on our map. Thus, each entry in our map matrix can be **one** of the 6 map types.
# 
# -	Transportation (T)
# -	Agricultural (A)
# -	Residential (R)
# -	Commercial (C)
# -	Water (W)
# -	Undeveloped land (U)
# 
# Our GIS will store the map information as a list of lists. If we have a list named **map**, then map[i][j] will store the map type at row i, column j. Each entry will contain a string that corresponds to 1 of the 6 possible map types listed above. The list representation of the map in **Figure 1** is shown below:

# ```
# [['A','A','A','A','U','U','U','U'],    
#  ['A','A','A','A','U','R','R','R'],    
#  ['W','W','W','W','T','T','T','T'],    
#  ['W','W','W','W','T','R','R','R'], 
#  ['C','C','U','U','T','R','U','U'],    
#  ['T','T','T','T','T','T','U','U'],    
#  ['U','U','U','U','T','R','U','U']]
# 
# ```
# 

# One usage of the system is to be able to easily identify whether or not a piece of land (entry in the map matrix) is deemed **commercially buildable**. A piece of land at **A<sub>ij</sub>** is deemed commercially buildable if the following conditions hold:
# -	The entry at **A<sub>ij</sub>** has map type **U**
# -	The entry **A<sub>ij</sub>** is not on the edges of the map (the first and last rows and columns).
# -	The entry **A<sub>ij</sub>** is not adjacent with an entry of map type **R** or map type **A**. Note that adjacent entries are entries to the top, bottom, left, and right of the current cell.
# 
# Based on the criteria and the map representation of **Figure 1**, it can be seen that **A<sub>4,2</sub>** is commercially buildable and **A<sub>1,4</sub>** is not commercially buildable.

# ---
# ## Additional Information (Important!)
# When using a 2D list, we can access elements around a specific index. Let's define a 3x3 2D list, **x**, seen below:

# <center>x =[[1,2,3], <br>
#      &nbsp; &nbsp; &nbsp;[4,5,6], <br>
#      &nbsp; &nbsp; &nbsp;[7,8,9]]</center>

# If we define variables **i**, and **j**, to both equal 1 for example, then **x[ i ][ j ]** would be **x[ 1 ][ 1 ]**, which in this 2D list is the integer _5_. We can access elements around this specific index by modifying our **i** and **j** variables. We can subtract or add 1 from **i** to access the elements above or below the original index. Addtionally, we can subtract or add 1 from **j** to access the elements to the left or right of the original index. To summarize:
#  
# - **x[ i-1 ][ j ]** would access the element <u>above</u> the original index. which here is _2_
# - **x[ i+1 ][ j ]** would access the element <u>below</u> the original index, which here is _8_
# - **x[ i ][ j-1 ]** would access the element <u>left</u> of the original index, which here is _4_
# - **x[ i ][ j+1 ]** would access the element <u>right</u> of the original index, which here is _6_

# ---
# Be careful when accessing adjacent elements - if you try to access an element that doesn't exist, you might receive an unexpected output, or an error! For example:

# - **x[ i-2 ][ j ]** which is equivalent to **x[ -1 ][ 1 ]**, would wrap around and give us the middle element in row **-1**, which here is the last row.
# - **x[ i ][ j+2 ]** Would try to access the element at **x[ 1 ][ 3 ]**, or in the nonexistent colum 3, which would produce an <u>error seen below!</u>
# 
# ```
# ----> 2 print(x[i][j+2])
# IndexError: list index out of range
# ```

# ---
# ## Program Requirements (12 Marks)
# 
# Your GIS system will be comprised of a set of functions used to analyze the information of any given map. In addition, you will be creating a function used to determine whether or not a piece of land is commercially buildable. The requirements of the system are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks.
# 
# 1. Define a function **count_type**(*map_data*, *map_type*):
#   - ***map_data***: A *list of lists* representing the data for a given map.
#   - ***map_type***: A *string* representing a map type ('T','A','R','C','W', or 'U')
#   - **Return:** An *integer* representing the number of times *map_type* occurs in *map_data*.
#   
#   
# 2.	Define a function **classify_map**(*map_data*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	**Return**: A map classification according to the following rules:
#           -	The *string* **Suburban** if the number of <u>'R' cells is greater than 50% of all cells.</u>
#           - The *string* **Farmland** if the number of <u>'A' cells is greater than 50% of all cells.</u>
#           - The *string* **Conservation** if the number of <u>'U' cells plus the number of 'W' cells is greater than 50% of all cells.</u>
#           - The *string* **City** if the number of <u>'C' cells is greater than 50% of all cells **and** the number of 'U' cells plus the number of 'A' cells is between 10% and 20% of all cells (inclusive).</u>
#           - The *string* **Mixed** if none of the above criteria are met.  
#           _(Hint, use your count_type function coupled with the fact that the total cells in map\_data is given by m*n)_
#           
# 
# 3.	Define a function **isolate_type**(*map_data*, *map_type*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	***map_type***: A *string* representing a map type (‘T’, ‘A’, ‘R’, ‘C’, ‘W’, or ‘U’)
#   -	**Return**: A <u>new</u> *list of lists* that represent *map_data* as a matrix but all entries that **are not** equal to *map_type* are replaced with a string containing only a space (" ").   
#   _(Hint, review the In-Lab Notebook <u>Nested Loops to Process Lists of Lists</u> demo on how to process 2D lists)_
#   
#   
# 
# 4.	Define a function **commercially_buildable**(*map_data*, *i*, *j*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	***i***: An *integer* representing a given row in *map_data*.
#   -	***j***: An *integer* representing a given column in *map_data*.
#   -	**Return**: **True** if *map_data[i][j]* ( **A<sub>ij</sub>**) is commercially buildable, otherwise **False**, according to the following rules from our background information:
#             -	First, ensure that the entry **A<sub>ij</sub>** is not at the edge of the map (the first and last rows and columns). If it is, return **False**. _(Hint, you will need to find the amount of rows and columns in the map for this step)_
#             -   Ensure that the entry **A<sub>ij</sub>** has map type **U**, otherwise return **False**.
#             -   Ensure the entry **A<sub>ij</sub>** is not adjacent with an entry of map type **R** or map type **A**. Note that adjacent entries are entries to the top, bottom, left, and right of the current cell. _(Hint, review the additional information section for this step)_

# ---
# ## Implementation
# Please define all functions in the cell below

# In[3]:


#********************************************
# Write your count_type function below: (2 marks)
#********************************************

# counts the number of cells in the map that have the same string as map_type
# returns the amount of that string detected as integer
def count_type(map_data, map_type):
    # initializes count variable for counting matching strings
    count = 0
    # for loops to iterate through each index in map_data
    for row in map_data:
        for index in row:
            if map_type in index:
                # adds to count when the index matches map_type
                count += 1
    return count # returns integer

#********************************************
# Write your classify_map function below: (4 marks)
#********************************************

# determines what type of terrain a map is
# returns either Suburban, Farmland, Conservation, City, or Mixed as strings
def classify_map(map_data):
    
    # defines total cell variable with total number of tiles on the map
    total_cells = len(map_data) * len(map_data[0])
    # sums number of undeveloped or water tiles on the map
    natural_land = count_type(map_data, 'U') + count_type(map_data, 'W')
    # sums number of undeveloped or agriculture tiles on the map
    open_land = count_type(map_data, 'U') + count_type(map_data, 'A')
    
    # checks number of tiles to see which map type map_data matches best
    if count_type(map_data, 'R') / total_cells > 0.5:
        return "Suburban"
    elif count_type(map_data, 'A') / total_cells > 0.5:
        return "Farmland"
    elif natural_land / total_cells > 0.5:
        return "Conservation"
    # checks if commercial tiles are over 50% of total tiles AND
    # if agriculture and undeveloped tiles are between 10% - 20% of the map
    elif count_type(map_data, 'C') / total_cells > 0.5 and 0.1 <= (open_land / total_cells) <= 0.2:
        return "City"
    # If nothing else matches, map is mixed
    else:
        return "Mixed"

#********************************************
# Write your isolate_type function below: (2 marks)
#********************************************

# replaces all map tiles not matching map_type with  " "
# returns an updated map as a list of lists
def isolate_type(map_data, map_type):
    
    # determines number of rows and columns in map_data
    rows = len(map_data)
    cols = len(map_data[0])
    
    # iterates through each index of every list in map_data
    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] != map_type:
                # replaces all indexes that don't match map_type
                map_data[i][j] = " "
                
    return map_data # returns list of lists

#********************************************
# Write your commercially_buildable function below: (2 marks)
#********************************************

# determines whether a tile on the map is approved for building commercial
# returns boolean depending on if map location is valid for building
def commercially_buildable(map_data, i, j):
    # determines number of rows and columns in map_data
    rows = len(map_data)
    cols = len(map_data[0])
    
    # Three IF statements were used here instead of AND operaters
    # this is because it would be crazy horzontally long if I used only AND
    if 0 < i < rows-1 and 0 < j < cols-1 and map_data[i][j] == 'U':
        # after checking if tile is on edge of map and if the tile is the correct type
        # program checks to make sure tiles above and below aren't residential or agri.
        if map_data[i-1][j] not in "RA" and map_data[i+1][j] not in "RA":
            if map_data[i][j-1] not in "RA" and map_data[i][j+1] not in "RA":
                # if all conditions satisfied, returns true, otherwise returns false
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# ---
# ## Testing
# 
# Unlike the other computing labs that required you to run main() to validate your code, these functions can act as stand-alone functions. You have been provided with some test cases, but you are encouraged to create more to thoroughly test your code.
# 
# ### Important
# 
# Run the cell where you implemented your functions first and ensure it outputs with no errors. Then, run the testing cell to verify that your code works correctly with the provided input. The following message should be printed after the testing cell is run:
# 
# ```
# The number of U spaces in MAP = 17  
# The number of T spaces in MAP2 = 12 
# MAP Type = Mixed 
# MAP2 Type = City  
# -----------------
# Isolated MAP: U
# [' ', ' ', ' ', ' ', 'U', 'U', 'U', 'U']
# [' ', ' ', ' ', ' ', 'U', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', 'U', 'U', ' ', ' ', 'U', 'U']
# [' ', ' ', ' ', ' ', ' ', ' ', 'U', 'U']
# ['U', 'U', 'U', 'U', ' ', ' ', 'U', 'U']
# -----------------
# Isolated MAP2: T
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# ['T', 'T', 'T', 'T', 'T', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', 'T', ' ', ' ', ' ']
# [' ', 'T', ' ', 'T', ' ', ' ', ' ']
# -----------------
# Is MAP commercially buildable at (4,2): True  
# Is MAP2 commercially buildable at (2,2): False
# ```
# 
# Again, note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell below is not graded, so feel free to modify the code as you wish!

# In[16]:


MAP = [['A','A','A','A','U','U','U','U'],
       ['A','A','A','A','U','R','R','R'],
       ['W','W','W','W','T','T','T','T'],
       ['W','W','W','W','T','R','R','R'],
       ['C','C','U','U','T','R','U','U'],
       ['T','T','T','T','T','T','U','U'],
       ['U','U','U','U','T','R','U','U']]

MAP2 = [['C','C','C','C','R','T','C'],
        ['T','T','T','T','T','C','C'],
        ['C','C','W','C','R','T','C'],
        ['C','C','C','W','U','T','C'],
        ['C','C','C','U','U','T','C'],
        ['C','C','C','C','C','U','C'],
        ['C','C','C','T','U','U','C'],
        ['C','T','C','T','U','A','C']]


# count_type() and classify_map() functions
print("The number of U spaces in MAP =",count_type(MAP, 'U'))
print("The number of T spaces in MAP2 =",count_type(MAP2, 'T'))
print("MAP Type =",classify_map(MAP))
print("MAP2 Type =",classify_map(MAP2))

# isolate_type() function
print("-----------------")
print("Isolated MAP: U")
MA = isolate_type(MAP,'U')
for row in MA:
    print(row)
print("-----------------")
print("Isolated MAP2: T")
MB = isolate_type(MAP2,'T')
for row in MB:
    print(row)
print("-----------------")

# commercially_buildable() function
print("Is MAP commercially buildable at (4,2):",commercially_buildable(MAP,4,2))
print("Is MAP2 commercially buildable at (2,2):",commercially_buildable(MAP2,2,2))


# ----------
# ## Code Legibility (6 Marks)
# Your code will be marked on commenting and code legibility.<br>
# The mark breakdown is as follows:<br>
# > - 2 marks for using **appropriate variable names** that indicate what is being stored in that variable<br>
# >- 2 marks for leaving **comments on major parts of your code** such as where you read the file or calculate a summation<br>
# >- 2 marks for **general legibility**. The TA's should be able to understand your code without spending hours reading it. For example do not put your code in one very long line as this is hard for someone else reading your code to understand

# ---
# ## Test Plan
# Develop a test plan for your program. Your test plan should have at least three test cases: one normal case, one boundary case, and one abnormal case. You can test any function but you must test **at least two different** functions. Please use the following format for your test cases:
# 
# **Function:**   
# **Input:**  
# **Output:**  
# **Expected Output:**  
# **Pass/Fail:**  
# 
# An example test case is shown below:  
# ```
# Function: count_type(map_data,map_type)
# Input: map_data = [['U','T','U','A'],
#                     ['R','T','W','A'],
#                     ['U','T','A','W']]  
#        map_type = 'U'
# Output: 3
# Expected Output: 3
# Pass/Fail: Pass
# ```
# 
# Implement your testing plan in the cell below! 

# ```
# DOUBLE CLICK TO EDIT THIS CELL. DO NOT DELETE QUOTATION MARKS
# TARCWU
# 
# NORMAL CASE:
# Function: count_type(map_data, map_type)
# Input: map_data = [['T','W','A','T'],
#                     ['W','A','R','T'],
#                     ['C','A','R','T']]
#        map_type = 'T'
# Output: 4
# Expected Output: 4
# Pass/Fail: PASS
# 
# BOUNDARY CASE:
# Function: count_type(map_data, map_type)
# Input: map_data = [['T','W','A','T'],
#                     ['W','A','R','T'],
#                     ['C','A','R','T']]
#        map_type = 'U'
# Output: 0
# Expected Output: 0
# Pass/Fail: PASS
# 
# ABNORMAL CASE:
# Function: count_type(map_data, map_type)
# Input: map_data = []
#        map_type = 'W'
# Output: 0
# Expected Output: 0
# Pass/Fail: PASS
# 
# 
# NORMAL CASE:
# Function: classify_map(map_data)
# Input: map_data = [['T','W','A','T'],
#                     ['W','A','R','T'],
#                     ['C','A','R','T']]
# Output: 'Mixed'
# Expected Output: 'Mixed'
# Pass/Fail: PASS
# 
# BOUNDARY CASE:
# Function: classify_map(map_data)
# Input: map_data = [['T','A'],
#                     ['T','A']]
# Output: 'Mixed'
# Expected Output: 'Mixed'
# Pass/Fail: PASS
# 
# ABNORMAL CASE:
# Function: classify_map(map_data)
# Input: map_data = []
# Output: IndexError: list index out of range
# Expected Output: 'Mixed'
# Pass/Fail: FAIL
# 
# ```

# ---
# ## Reflective Questions (6 Marks)
# 
# 1. Which functions did you use a nested structure (nested loops, nested conditionals, etc) to implement the requirements? Would it have been possible to implement them without using a nested structure? Which functions did you *not* use a nested structure? Would it have been possible to implement them *with* a nested structure?  
# 
# 
# 2. Suppose we wanted to create an additional map classification called 'Urban City' which is indicated by the number of 'R' cells plus the number of 'C' cells being between 60% and 80%. Can we do this? How might this affect our classify_map() function?
# 
# 
# 3. How many test cases would you need to confirm that your classify_map() function correctly identifies a "Farmland" map? Explain what your test cases would be.

# ```
# DOUBLE CLICK TO EDIT THIS CELL. DO NOT DELETE QUOTATION MARKS
# 
# 1. I used nested structures for count_type, isolate_type, and commercially_buildable. I don't believe it's possible to implement count_type or isolate_type without nest structures, as I needed to iterate through a list of lists. In commercially_buildable, it was possible to avoid the nested structions and use comparators like AND. However, my code would have been very long horizontally so I opted for nested conditionals.
# classify_map did not use any nested structures, only an if statement with many elif statements. A nested structure could have been used when the function determined if map_data is a city. The and in the elif statement could be replaced with an if statement inside a preliminary if statement.
# 
# 2. Yes, we can do this. I would create another variable which sums the number of 'R' and 'C' cells in the map. If that variable divided by the total number of cells is between 0.6 and 0.8, I would classify the map as an 'Urban City'. The conditional that would check the map to determine 'Urban City' will come before it checks for 'Suburban' or 'City'. This way, if the function finds an urban city, it will stop and return 'Urban City'. If it does not find an urban city, it will still check if the map is a 'City' or 'Suburban'.
# 
# 3. I would use 4 test cases. The first two test cases would be normal cases, one would be expected to output 'Farmland', the other expected to output anything other than farmland. The third test case would be a boundary case, where I would test the only boundary of 0.5 by inputting a map with 50% agriculture tiles. This test case would be expected NOT to output farmland. Finally, I would use the abnormal case to test a completely empty list (eg. list = []) which would be expected NOT to output farmland.
# 
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 6 dropbox on avenue with the naming convention: macID_CL6.py
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
