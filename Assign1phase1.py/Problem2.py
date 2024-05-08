""" 

Problem: Knock Knock are you there?

Input Format:

1. Take M int input from the User 
2. Get M , seperated values from a user 
3. Enter a number 'N' you are looking for

Output Format:

1. Print index on console once Found or Print 'Better Luck Next Time' to the console


"""

M = int(input())

input_str = input()

element_list = []
element = ''
for char in input_str:
    if char == ',':
        element_list.append(element)
        element = ''
    else:
        element += char

if element:  
    element_list.append(element)

N = input()

last_index = -1  # Initialize last index to -1
for i in range(len(element_list)):
    if int(N) == int(element_list[i]):
        last_index = i  # Update last index when the element is found
        found = True

if last_index != -1:
    print(last_index)
else:
    print("Better Luck Next Time")