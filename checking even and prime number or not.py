def isEven(a):
    if a%2 == 0:
        print("The given number",a,"is an Even number")
    else:
        print("The given number",a,"is not an Even number")

def isPrime(a):
    if a==1:
        print(a,"is not a prime number")
    elif a>1:
        for i in range(2,a):
            if(a%i) == 0:
                print(a,"is not a prime number")
            else:
                print(a,"is a prime number")
                break
    else:
        print(a,"is not a prime number")
    
a=int(input("Enter a number : "))

even = isEven(a)
prime = isPrime(a)
