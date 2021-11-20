 #****************************************************************************
 # Author:              Loic Konan 
 # Email:               loickonan.lk@gmail.com 
 # Label:               Question 1 
 # Title:               Programing Assignment 05 
 # Course:              CMPS 4143 
 # Semester:            Fall 2021 
 # Date:                11/22/2021
 # 
 # Description:     
 #		        You need to implement the stack with Linkedlist data 
 # 			structure in python. Implement the stack means, 
 #                      all of the stack functionalities including the 
 #                      construction of stacks should present on your code.
 #				    
 # 
 # Solution:				
 # 			My stack data structure has following functionalities: 
 #
 # 			- empty()       => Returns whether the stack is empty.
 #			- size() 	=> Returns the size of the stack.
 # 			- top() 	=> Returns a reference to top element.
 # 			- push() 	=> Inserts the element at the top of the stack.
 # 			- pop() 	=> Deletes the topmost element of the stack. 
 #			- getMin() 	=> Retrieving the minimum element in the stack.
 #
 #                      Each of these functions have a Constant complexity O(1) 
 #                  
 #
 # Files:               Question1.py
 # 
 #****************************************************************************/
 
 
class Node:
        
        def __init__(self, value):
                self.value = value
                self.next = None

class MinStack:
        
        def __init__(self):
                self.head = None
                self.min = float('inf')

        def push(self, value):
                if self.head == None:
                        self.head = Node(value)
                        self.min = value
                else:
                        if value >= self.min:
                                n = Node(value)
                                n.next = self.head
                                self.head = n
                        else:
                                v = 2 * value - self.min
                                n = Node(v)
                                n.next = self.head
                                self.head = n
                                self.min = value


        def pop(self):
                if self.head:
                        if self.head.value < self.min:
                                self.min = self.min * 2 - self.head.value
                        self.head = self.head.next

        def top(self):
                if self.head:
                        if self.head.value < self.min:
                                self.min = self.min * 2 - self.head.value
                                return self.min
                        else:
                                return self.head.value
                else:
                        return -1

        def getMin(self):
                if self.head:
                        return self.min
                else:
                        return "The Stack is Freaking Empty"
                
        def empty(self):
                if self.head == None:
                        return True
                else:
                        return False
        
        # # Prints out the stack	
        # def display(self):
                
        #         iternode = self.head
        #         if self.empty():
        #                 print("Stack Underflow")
                
        #         else:
                        
        #                 while(iternode != None):
                                
        #                         print(iternode.value,"->", end = " ")
        #                         iternode = iternode.next
                                
# Driver code
MyStack = MinStack()

# Inserting few elements to the stack
print('''
################################### 
################################### 
###### Inserting Elements ######### 
################################### 
################################### 
      ''')
MyStack.push(-2)
print("\tNumber Inserted -2")

MyStack.push(0)
print("\tNumber Inserted  0")

MyStack.push(-3)
print("\tNumber Inserted -3")

# Print top element of stack
print('''
################################### 
################################### 
########## Min element  ########### 
################################### 
################################### 
      ''')
print("\t     ", MyStack.getMin())


MyStack.pop()

# Inserting few elements to the stack
print('''
################################### 
################################### 
###### Inserting Elements ######### 
################################### 
################################### 
      ''')
MyStack.push(50)
print("\tNumber Inserted 50")

MyStack.push(-20)
print("\tNumber Inserted -20")

MyStack.push(13)
print("\tNumber Inserted 13")

MyStack.pop()


# Print top element of stack
print('''
################################### 
################################### 
########## Min element  ########### 
################################### 
################################### 
      ''')
print("\t     ", MyStack.getMin())