"""
Design of Functions with only one parameter or no-parameter (T-Shirt Brand)
While executing, get help from a helper function call that invokes a function block which asks for
a User Name.
In the case of Availability of Brand
Greet The User Saying: “ Hi {name of the user}, the brand you are looking for is available in our
store ”
In the case of Non Availability of Brand
Greet The User Saying: “ Hi {name of the user}, Unfortunately the brand you are looking for is not
available in our store ”
Get the name of function using another function
Helper Function name—> get_name() 
This problem statement is subject to only single Function call —> get_tshirt(brand_name)

"""

li=[]
M=int(input())
x=input()
i=0
while i<len(x):
    if x[i]!=';':
        if x[i]=='+':
            li.append(int(x[i+1]))
            i+=1
        elif x[i]=='-':
            li.append(-int(x[i+1]))
            i+=1
        else:
            li.append(int(x[i]))
    i+=1

add=0
for i in range(0,M):
    add=add+li[i]
print(add)
li
