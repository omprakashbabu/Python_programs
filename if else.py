def Sum_of_two_numbers(a,b):
    return a+b

def Sum_of_three_numbers(a,b,c):
    return a+b+c
    
choice = int (input ("Enter 2 for sum of two numbers or 3 for sum of three numbers : "))

if choice == 2:
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    result=(Sum_of_two_numbers(a,b))
    print("The sum of two numbers is ",result)
elif choice == 3:
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    c=int(input("Enter the third number : "))
    result=(Sum_of_three_numbers(a,b,c))
    print("The sum of three numbers is ",result)
else:
    print("Invalid input")  
    
if 120 < result < 320:
    print("200 is returned because the sum lies between 120 and 320")
else:
    print("The sum does not lies between 120 and 320")
    

