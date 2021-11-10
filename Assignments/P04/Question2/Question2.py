 #****************************************************************************
 # Author:          Loic Konan 
 # Email:           loickonan.lk@gmail.com 
 # Label:           Question 2 
 # Title:           Programing Assignment 04 
 # Course:          CMPS 4143 
 # Semester:        Fall 2021 
 # Date:            11/10/2021
 # 
 # Description:     
 #                  Given an array of strings strs, group the anagrams together. 
 #                  You can return the answer in any order.
 #  
 #                    - Input type: A list with words 
 #                    - Output type: A list of lists with grouping the anagrams together
 #                  
 # Solution:        
 #                  Used
 #                  
 #
 #
 # Files:           Question2.py
 # 
 #****************************************************************************/
 
 # Any solution that works only for the letters a-z is a bad solution
 # because it is not sufficiently generic at all. 
 # There are many other characters that exist besides a-z
 
# define the function definition and it processes
# will be calle whenever the function is being mention inside of the main
# portion of our program
def anagrams(Values):
    Dictionary = {}
    #Loop through all items in the list
    for i in Values:
        #Sort the word
        key = ''.join(sorted(i))
        #We must check to make sure the word doesnt exist already
        if key not in Dictionary:
            Dictionary[key] = []
        #add the word to the group
        Dictionary[key].append(i)
    #convert the dictionary values to a list and return them
    return [Values for key,Values in Dictionary.items()]


#------- main portion of our program-----------------

    # read in the first string
StringList = ['eat','tea','tan','ate','nat','bat']
print(anagrams(StringList))
# reading the second sample string
StringList = ['']
# go to function definition to determine the output
print(anagrams(StringList))

# reading the thir string 
StringList = ['a']
print(anagrams(StringList))

# now we create a prompt for user to try
userlist = [] 
userlist = [item for item in input("Lets test yours : ").split()]
# see if any matches found
print(anagrams(userlist))

