"""With reference to the Problem Statement_01 in this task students have to create an optional
argument to the function get_tshirt() with size as one of the parameters."""

def get_tshirt():
    user_name = input("Enter Your Name: ")
    brand_name = input("Enter the brand you are looking for: ")
    size = input("Enter the size you are looking for (optional): ") 
    check_brand(user_name, brand_name, size)  
    
def check_brand(user_name, brand_name, size=None): 
    available_size=["M,L,XXS,XS,XL"]
    brand_list = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour"]
    if brand_name in brand_list:
        if size:
            print(f"Hi {user_name}, The brand {brand_name} in size {size} is available in our store.")
        else:
            print(f"Hi {user_name}, The brand {brand_name} you are looking for is available in our store.")
    else:
        print(f"Hi {user_name}, Unfortunately the brand {brand_name} you are looking for is not available in our store")

get_tshirt() 

