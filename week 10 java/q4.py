def isEven(a):
    if a%2 == 0:
        print("The given number",a,"is an Even number")
    else:
        print("The given number",a,"is an Odd number")

def isPrime(a):
    flag=0
    if a==1 or a==0:
        print(a,"is not a prime number")
    else:
        for i in range(2,a):
            if(a%i) == 0:
                flag =1
            else:
                continue
        if flag==1:
            print("The given number is not a prime number")
        else:
            print("The given number is a prime number")
                        
    
    
a=int(input("Enter a number : "))
even = isEven(a)
prime = isPrime(a)