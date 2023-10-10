def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
p=int(input("Enter a number : "))
print("The factorial of the given number is",factorial(p))
