def max_of_three_numbers(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return 
    
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))

max=max_of_three_numbers(a,b,c)
print("The maximum of three numbers is ",max)
