 #****************************************************************************
 # Author:          Loic Konan 
 # Email:           loickonan.lk@gmail.com 
 # Label:           Question 2 
 # Title:           Programing Assignment 03 
 # Course:          CMPS 4143 
 # Semester:        Fall 2021 
 # Date:            10/20/2021
 # 
 # Description:     
 #                  This program will asks the user to enter the number of people, 
 #                  then based on this number it will iterate that amount of time  
 #                  where each time it will get a single person’s information 
 #                  like First Name, then Last Name, Age, Occupation and Address.
 #                  Then finally it will Display the user details one by one.
 # 
 # Solution:        
 #                             
 #
 # Files:           Question2.py
 # 
 #****************************************************************************/

Fname_array = list()                                                # This is a list for the First name.
Lname_array = list()                                                # This is a list for the Last Name.
age_array = list()                                                  # This is a list for the the age.
Occupation_array = list()                                           # This is a list for the occupation.
Address_array = list()                                              # This is a list for the address.


# If this while loop is true, we then ask the user
# to enter a number and we make sure that it is a number
# if not we print an error message.
while True:
        number = input("How many people do you need store their information? ")
        if number.isdigit():                                        # if the input enter is a number break out of the loop.
            break
        else: print("Please Enter a valid Number: ")                # if the input enter is not a number print that message.
        
        
# Using this for loop to iterate as many time as
# that number entered by the user.        
for x in range(0, int(number)):    
    
    # Using this while loop to prompt the user for his Last name.
    # Then check if the name is valid or not.
    while True:
        LName = input("\nEnter the Last Name of person number " + str(x+1) + " : ")
       
        if LName.isdigit():                                         # if the input enter is numberic print that message.
            print("Please Enter a valid age person number " + str(x+1) + " : ")
        else: break
    
    
    # Using this while loop to prompt the user for his First name.
    # Then check if the name is valid or not.
    while True:
        FName = input("Enter the First Name of person number " + str(x+1) + ": ")
        
        if FName.isdigit():                                          # if the input enter is numberic print that message.
            print("Please Enter a valid Last Name person number " + str(x+1) + " : ")
        else: break
    
    
    # Using this while loop to prompt the user for his Age.
    # Then check if the Age is valid or not.
    while True:
        Age = input("Enter the age of person number " +  str(x+1)  + " : ")
        
        if Age.isdigit() and (0 < int(Age) < 150):                    # if the input enter is a number break out of the loop.
            break
                                                                      # if the input enter is not a number then print that message.
        else: print("Please Enter a valid age person number " + str(x+1) + " : ")
            
            
    # Using this while loop to prompt the user for his Occupation.
    # Then check if the Occupation is valid or not.      
    while True:        
        Occupation = input("Enter the occupation for person number " + str(x+1) + " :")
        
        if Occupation.isdigit():                                       # if the input enter is numberic print that message.
            print("Please Enter a valid Occupation person number " + str(x+1) + " : ")
        else: break
    
    
    # Using this while loop to prompt the user for his address.
    # Then check if the address is valid or not. 
    while True:
        address = input("Enter the address for person number " + str(x+1) + " :")
       
        if address.isdigit():                                          # if the input enter is numberic print that message.
            print("Please Enter a valid address person number " + str(x+1) + " : ")
        else: break
        
    
    Lname_array.append(LName)                                          #
    Fname_array.append(FName)                                          #
    age_array.append(Age)                                              #
    Occupation_array.append(Occupation)                                #
    Address_array.append(address)                                      #
    
print("\n\nOutput: \n")
 
 
 # Using this for loop iterate through my different list
 # then display the each store values to the console. 
for x in range(0,int(number)):    
    print(Lname_array[x], Fname_array[x], ", aged", age_array[x]," years, worked as a ",Occupation_array[x],
             " and currently lives at ",Address_array[x],".\n")
 