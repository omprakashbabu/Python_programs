def c_to_f(c):
    return (c*9/5)+32

def f_to_c(f):
    return (f-32)*(5/9)

choice=int(input("Enter 1 to find value of celsius to farenheit or enter 2 to find value of farenheit to celsius : "))

if choice == 1:
    n=float(input("Enter the celsius : "))
    print("The farenheit is ",c_to_f(n))
    
elif choice == 2:
    m=float(input("Enter the farenheit : "))
    print("The celsius is ",f_to_c(m))
else:
    print("Invalid input")