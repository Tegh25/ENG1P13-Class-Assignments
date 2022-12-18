#!/usr/bin/env python
# coding: utf-8

# # Computing 7 Assignment
# 
# 

# ---
# ## Background
# 
# In this assignment, you will be extracting daily temperature data, sorting the data, and then calculating the median temperature for a given set of data.
# 
# A set of daily temperature data will be provided to you as a *list* of strings. For example:
# 
# <br>
# <center><code>temps = ["5","-1.0","1.1","None","9","NA","1.0"]</code></center>
# <br>
# 
# Note that the temperature may not be recorded on some days. A sequence of characters that cannot be represented as a number indicate that the temperature was not recorded on a given day. In the previous example, we can see that the strings "None" and "NA" were used to represent days where the temperature was not recorded. It is important to note that these strings can consist of any characters and can vary in length. Some more examples would be "" (the empty string), "Nothing", "Not recorded", "Forgot", etc.
# 
# To calculate the median temperature for a given set of data, we first need to convert the data to a list of float numbers. The data converted from the *temps* list is given below. Notice how the days that did not have a recorded temperature were ignored:
# 
# <br>
# <center><code>temps_extracted=[5.0,-1.0,1.1,9.0,1.0]</code></center>
# <br>
# 
# How would we calculate the median of our list? Recall that the median is a value separating the higher half from the lower half of a list of sorted values. In the case where the length of our list of numbers is odd, the median is the middle element in our list. In the case where the length of our list of numbers is even, the median can be found by taking the average of the two center most elements. 
# 
# We cannot calculate the median until we sort our values. Our sorted temperatures will look as follows:
# 
# 
# <br>
# <center><code>temps_sorted=[-1.0,1.0,1.1,5.0,9.0]</code></center>
# <br>
#   
#     
# Now that our list is sorted, we can see that the median in this case is **1.1**.
# <br>
# 
# ---
#     
# So how do we sort a list of values? Formally, a sorting algorithm is a sequence of steps that are used to sort a sequence of values. It turns out that there exist many different sorting algorithms, some more complicated than others. In todays assignment we are going to focus on an intuitive sorting algorithm known as **selection sort**. We are going to use this algorithm to sort a list of numbers in ascending order.
# <br>
#     
# Say we have a list named *nums*. The main idea of selection sort is that we want to start iterating over our list *nums* from i = 0 to the length of our list minus 1 (n-1), choosing the smallest element in the sub list from *nums[i]* to *nums[n-1]* and placing it in *nums[i]* on each iteration. If you are confused, don't worry! We have provided you the pseudocode for the algorithm. Before looking at the pseudocode, use the following example to gain some intuition about how selection sort works.
# <br>
# <br>
# 
# Imagine that we have the following list of numbers that need to be sorted:
# 
# ![alg%20%2826%29.png](attachment:alg%20%2826%29.png)
# 
# 
# We start sorting at the left most item. We call our current position index i. The left most element in our list is the number 2, which occurs at i = 0.
# 
# ![alg%20%2825%29.png](attachment:alg%20%2825%29.png)
# 
# When considering the final sorted list, should the number 2 be in this position? What is the smallest element in our list from index i to the end of our list (index 4)? By inspection, we can see that the smallest number is 1. We can identify the position of this number using the variable min_index, which in this case is min_index = 2. Therefore the number 1 should be at index i because it is the smallest element in our list from index 0 to index 4!
# 
# ![alg%20%2824%29.png](attachment:alg%20%2824%29.png)
# 
# We can guarantee that the number 1 will be in the correct position in our final sorted list if we swap the elements at i and min_index! 
# 
# ![alg%20%2823%29.png](attachment:alg%20%2823%29.png)
# 
# You might think that 2 is still not in its correct position, but don't worry! We can guarantee that the number 1 is in the correct position, and we will worry about 2 later.
# <br>
# <br>
# 
# Let's now increment i to 1.
# ![alg%20%2821%29.png](attachment:alg%20%2821%29.png)
# 
# Let's perform the same actions we did when i was 0. What is the smallest element in our list from the element at this position (i = 1) to the end of our list (index 4)? By inspection, we can see that the smallest number is 2 which occurs at index 2, thus min_index = 2 in this case.
# 
# ![alg%20%289%29.png](attachment:alg%20%289%29.png)
# 
# We then swap the elements at i and min_index!
# 
# ![alg%20%2811%29.png](attachment:alg%20%2811%29.png)
# 
# Let's now increment i once again to 2.
# 
# ![alg%20%2812%29.png](attachment:alg%20%2812%29.png)
# 
# Can you see what's going on here? All of the elements (green) to the left of our current index i are sorted! Therefore our entire list will be sorted if we continue with this algorithm until we reach the end of our list. The following illustrations demonstrate how the algorithm will perform for the rest of the list.
# 
# ![alg%20%2820%29.png](attachment:alg%20%2820%29.png)
# ![alg%20%2814%29.png](attachment:alg%20%2814%29.png)
# 
# Increment i once again.
# 
# ![alg%20%2815%29.png](attachment:alg%20%2815%29.png)
# ![alg%20%2819%29.png](attachment:alg%20%2819%29.png)
# ![alg%20%2817%29.png](attachment:alg%20%2817%29.png)
# 
# When we increment i one last time, we reach the end of our list and all elements are sorted!
# 
# ![alg%20%2818%29.png](attachment:alg%20%2818%29.png)
# 
# <br>
# 
# The pseudocode for the algorithm is given below. We assume that the list we are sorting is given by the name *nums*.
# ```
# Create a variable n and set it equal to the length of nums
# For i = 0 to n-1
#     Create a variable min_index, and set it equal to i
#     For j=i to n-1
#         if nums[j] is less than nums[min_index] then set min_index to j
#     endFor
#     Swap the elements at nums[i] and nums[min_index]
# endFor
# ```
# 
# It is your task to implement the sorting algorithm from the pseudocode, as well as other functions listed in the requirements section of this document.

# ---
# ## Program Requirements (12 Marks)
# 
# The requirements of the system are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks. You can choose to copy and paste the function names into the implementation cell to avoid spelling mistakes.
# 
# ***Note: you must include a try and except statement in at least two functions in your code.***
# 
# 1.	Define a function **selection_sort**(*nums*):
#   -	***nums***: A *list* of floats.
#   -	**Return**: A sorted copy of the list *nums* using the selection sort algorithm.
#       <br>*Note: Make sure that you sort a copy of the list. DO NOT modify the original list. You can create a copy of nums by writing the code new_arr = nums.copy(). In addition, marks will not be given if the selection sort algorithm is not used. Pseudocode of the selection sort sorting algorithm is provided above in the Background section.*  
#   
# 
# 2.	Define a function **extract_temps**(*temps*):
#   - ***temps***: A *list* of *strings* representing a set of daily temperatures. 
#   -	**Return**: A *list* of numeric items that represent, where applicable, each element in **temps** converted to a float
#   <br>*Note: Some of the items in temps cannot be represented as a float. These items should be ignored. Refer to the background section as an example*
#   
#  
# 3.	Define a function **calculate_median**(*nums*):
#   -	***nums***: A *list* of sorted floating numbers.
#   -	**Return**: A *float* representing the median of nums.
#   <br>*Hint: If the length of a sorted list is odd then the median exists at index n//2 where n is the length of the list and // represents integer division. If the length of a sorted list is even, the median is calculated by the average of the two most middle elements. One of these elements exists at index n//2, can you figure out the other one? For example, the median of [1.0,2.0,3.0,4.0] is (3.0+2.0)/2 = 2.5*
#   
#   
# 4. Define a function **main**(*temp_data*):
#   -	***temp_data***: A *list* of *strings* representing a set of daily temperatures. 
#   -	**Return**: A *float* representing the median of nums. Return the *string* "N/A" if an error occurs.

# ---
# ## Implementation
# 
# Please define all functions in the cell below

# In[47]:


#********************************************
# Write your selection_sort function below: (4 marks)
#********************************************

# sorts list into order of least to greatest
# inputs list of integers/floats, outputs sorted list of int/floats
def selection_sort(nums):
    # copy list into another for use, saves length of list
    new_arr = nums.copy()
    n = len(new_arr)
    
    # iterates through each index of list
    # replaces index with the smallest value it finds
    for i in range(n-1):
        # resets saved index value of selected index
        min_index = i
        
        # iterates through list to find a value smaller than initial index
        for j in range(i, n-1):
            if new_arr[j] < new_arr[min_index]:
                # saves new smallest value if found
                min_index = j
                
        # swaps the values of the current index and lowest index found
        index_i = new_arr[i]
        index_min = new_arr[min_index]
        new_arr[i] = index_min
        new_arr[min_index] = index_i
    
    return new_arr # returns copied version of list

#********************************************
# Write your extract_temps function below: (3 marks)
#********************************************

# removes non-float convertable values from list
# inputs list, outputs list of floats or empty list
def extract_temps(temps):
    # initializes variable to store extracted float values
    temps_extracted = []
    
    # iterates through each index of input list
    for data in temps:
        # if variable is a float or float convertable it will save it
        try:
            temps_extracted.append(float(data))
        # if it can't be a float, it will return and catch an error and move to next index
        except:
            next
    
    return temps_extracted # returns list of floats

#********************************************
# Write your calculate_median function below: (4 marks)
#********************************************

# calculates median (middle value or average of middle values) value of a list of int/floats
# inputs list of integers/floats (preferably sorted), outputs median value as float
def calculate_median(nums):
    # if there's not an even number of indexes in the list
    if len(nums) % 2 != 0:
        # return the value in the middle of the list as float
        return nums[len(nums)//2]
    # otherwise list has an even number of indexes
    else:
        # return average of both middle values in list as float
        median = nums[len(nums)//2] + nums[len(nums)//2 - 1]
        return median / 2

#********************************************
# Write your main function below: (1 mark)
#********************************************

# main function for organizing weather data from a list
# inputs list with any types in it, outputs calculated median of list or N/A
def main(temp_data):
    # try to calculate median of inputted list using functions defined above
    try:
        temp_extracted = extract_temps(temp_data)
        temp_sorted = selection_sort(temp_extracted)
        return calculate_median(temp_sorted)
    # if median cannot be calculated (error) return "N/A"
    except:
        return "N/A"


# ---
# ## Testing
# Unlike the other computing labs that required you to run main() to validate your code, these functions can act as stand-alone functions. You have been provided with some test cases, but you are encouraged to create more to thoroughly test your code.
# 
# ### Important
# 
# Run the cell where you implemented your functions **first** and ensure it outputs with no errors. Then, run the testing cell to verify that your code works correctly with the provided input. The following message should be printed after the testing cell is run:
# 
# ```
# Given Temps: ['5', '', '5.5', '6.2', '4.5', 'N/A', 'Not Recorded', '5.67']
# Median: 5.5
# -----
# Given Temps: ['5', 'N/A', '5']
# Median: 5.0
# -----
# Given Temps: ['-10', '', '']
# Median: -10.0
# -----
# Given Temps: ['', '', '']
# Median: N/A
# ```
# Again, note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell below is not graded, so feel free to modify the code as you wish!

# In[48]:


temps = ["5","","5.5","6.2","4.5","N/A","Not Recorded","5.67"]
print("Given Temps:",temps)
print("Median:",main(temps))
print("-----")
temps = ["5","N/A","5"]
print("Given Temps:",temps)
print("Median:",main(temps))
print("-----")
temps = ["-10","",""]
print("Given Temps:",temps)
print("Median:",main(temps))
print("-----")
temps = ["","",""]
print("Given Temps:",temps)
print("Median:",main(temps))


# ---
# ## Code Legibility (6 Marks)
# Your code will be marked on commenting and code legibility.<br>
# The mark breakdown is as follows:<br>
# > - 2 marks for using **appropriate variable names** that indicate what is being stored in that variable<br>
# >- 2 marks for leaving **comments on major parts of your code** such as where you read the file or calculate a summation<br>
# >- 2 marks for **exception handling** (for at least 2 functions). Your functions should produce the required outputs even when receiving unexpected inputs

# ---
# ## Test Plan (6 Marks)
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
# Function: extract_temps(temps)
# Input: temps = ["1","NA","5.5"]  
# Expected Output: [1.0,5.5]
# Output: [1.0,5.5]
# Pass/Fail: Pass
# ```
# 
# Implement your testing plan in the cell below! 

# ```
# DOUBLE CLICK TO EDIT THIS CELL. DO NOT DELETE QUOTATION MARKS
# 
# NORMAL CASE
# Function: extract_temps(temps)
# Input: temps = ["2","NA","6.5"]  
# Expected Output: [2.0,6.5]
# Output: [2.0,6.5]
# Pass/Fail: Pass
# 
# BOUNDARY CASE
# Function: extract_temps(temps)
# Input: temps = []  
# Expected Output: []
# Output: []
# Pass/Fail: Pass
# 
# ABNORMAL CASE
# Function: extract_temps(temps)
# Input: temps = 420
# Expected Output: TypeError
# Output: TypeError
# Pass/Fail: Pass
# 
# 
# 
# NORMAL CASE
# Function: calculate_median(nums)
# Input: nums = [1,2,3,4,5,6,7]  
# Expected Output: 4
# Output: 4
# Pass/Fail: Pass
# 
# BOUNDARY CASE
# Function: calculate_median(nums)
# Input: nums = []  
# Expected Output: IndexError
# Output: IndexError
# Pass/Fail: Pass
# 
# ABNORMAL CASE
# Function: calculate_median(nums)
# Input: nums = "This is an abnormal input cause it expects a list of sorted integers"
# Expected Output: TypeError
# Output: TypeError
# Pass/Fail: Pass
# 
# ```

# ---
# ## Reflective Questions
# 
# 1. What input would cause your main() function to return "N/A"?
# 
# 
# 2. Assuming that functions 1-3 are only used inside your main function, is it necessary to use try and except statements inside them to validate input?

# ```
# DOUBLE CLICK TO EDIT THIS CELL. DO NOT DELETE QUOTATION MARKS
# 
# 1. Any list input that does not have a single index that can be converted to a float will return "N/A". This is because all the values that can't be converted to a float will be removed, and a list with length of 0 will cause an error in the calculate_median function, resulting in the main function catching the error and returning "N/A".
# 
# However, strings that can be converted to floats will not produce an error, any other kind of string or any other input type will cause the main function to return "N/A".
# 
# 2. For the extract_temps function, it is necessary to use try and except statements inside that function because we need to be able to analyze each index of a list to find a value that can be converted to a float. Either this works successfully, or produces an error, and we need to catch the error for our whole program to work properly.
# 
# We can change the extract_temps function to not need a try and except statement. This would only be possible if we put the for loop and try and except statement in the main function and if we changed extract_temps to only check one index of a list rather than all of them.
# 
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 7 dropbox on avenue with the naming convention: macID_CL7.py
# 
# #### NOTE THAT YOU WILL BE MARKED ON MULTIPLE ITEMS IN THIS LAB IN ADDITION TO THE FUNCTIONALITY OF YOUR CODE
#  - Variable Names
#  - Commenting
#  - General Legibility
#  - Try and Except
#  - Test Plan
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely receive zero.**
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST
# 
# Late labs will not be accepted
