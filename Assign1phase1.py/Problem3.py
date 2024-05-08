"""
Problem 3: Reflection or Pratibimb 

Design and Develop a User Defined function named (reflection) pass the input literal 'Welcome to EN2004' and return Output Format Mentioned Below

Input Format:

1. Take M str input from the User 
2. Get M , seperated str literals from a user (Test string to pass: 'Welcome to EN2004')

Output Format:

EN2004
to
Welcome



"""

m = int(input())

def reflection(value):
    words = []
    word = ''
    for char in value:
        if char != ',':
            word += char
        else:
            words.append(word)
            word = ''
    words.append(word)
    for i in range(len(words)-1, -1, -1):
        print(words[i])

input_str = input()
reflection(input_str)