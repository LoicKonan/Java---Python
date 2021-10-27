 #****************************************************************************
 # Author:          Loic Konan 
 # Email:           loickonan.lk@gmail.com 
 # Label:           Question 3 
 # Title:           Programing Assignment 03 
 # Course:          CMPS 4143 
 # Semester:        Fall 2021 
 # Date:            10/20/2021
 # 
 # Description:     
 #                  
 # 
 # Solution:
 #
 # Files:           Question3.py
 # 
 #****************************************************************************/


# creating the definition for myAtoi(passing in the string s inside)
def myAtoi(s):
    # declare a variable to check the number is positive or negative
    PositiveNumber = True

    # storing the string into in string
    InputValueString = ""
    
    # if there is nothing in the string return
    if len(s) == 0:
        return 0
    i = 0

    # if first char after whitespace is a digit, add to string input
    # if is a + sign dont do anythin if there is a negative sign
    # positive value is changed to false. all other cases, return
    if i < len(s):
        if ord('0')<= ord(s[i])<= ord('9'):
            InputValueString += s[i]
        
        elif s[i] == "-":
            PositiveNumber = False # if negative then positive number set to false
        
        elif s[i] == "+":  # else if as elif
            pass
        
        else:
            return 0
    
    # increment i by 1 that is move ahead one step of the first character after white spaces
    i+=1

    # now run a loop till the end of the string
    while i < len(s):
        # if char is a number add to string input
        if ord('0')<= ord(s[i])<= ord('9'):
            InputValueString += s[i]
        # else, break the loop
        else:
            break
        i+=1
    
    # if the resulting string is empty, return 0
    if len(InputValueString) == 0:
        return 0
    
    # else check InputValueString
    else:
        # return minimum of int(InputValueString) and 2**31-1
        if PositiveNumber:
            
            return min(int(InputValueString),2**31-1)
        # return max of -1*int(InputValueString) and -2**31-1
        return max(-1*int(InputValueString), -2**31)
 
try:
    s = str(input("Please enter a string of values: "))
    myAtoi(s)

except:
    print("invalid data unable to process")


print('Input:    "',s,'"',"\t\t",'OutPut:    ',myAtoi(s.lstrip()),'\n') 
