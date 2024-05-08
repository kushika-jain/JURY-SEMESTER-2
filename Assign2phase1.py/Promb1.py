"""
Design a power() function that must take two parameters base and exponent design a solution.
1. Use a function call within the function to get the desired outcome as discussed in the
classroom interactions on recursive calls.
2. Discuss your solution and problems it may have? (Like: Maximum Recursion Depth Exceed)
3. How to over come it (With valid proof of concept) Justify it by drawing Recursion Tree 

"""

def power(base, exponent):
  if exponent == 0:
    return 1
  else:
    return base * power(base, exponent-1)
