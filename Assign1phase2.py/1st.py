"""School of Engineering
Department of CSE
Assignment_01_Phase-II
Introduction to Computing
Course Lead - EN2004
Author-Rushikesh Pawar
Problem Statement_01
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
This problem statement is subject to only single Function call —> get_tshirt(brand_name)"""

def get_tshirt():
    user_name = input("Enter Your Name: ")
    brand_name = input("Enter the brand you are looking for: ")
    check_brand(user_name, brand_name)

def check_brand(user_name, brand_name):
    brand_list = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour"]
    if brand_name in brand_list:
        print(f"Hi {user_name},The brand you are looking for is available in our store.")
    else:
        print(f"Hi {user_name},Unfortunately the brand {brand_name} you are looking for is not available in our store")

get_tshirt()



