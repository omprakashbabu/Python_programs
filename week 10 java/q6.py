nterms = int (input ("Enter the number of terms to be generated : "))

n1,n2 = 0,1
count = 0

if nterms <= 0:
    print("Invalid input , enter a positive number")
elif nterms == 1:
    print("Fibonacci series upto ",nterms," :")
    print(n1)
else:
    print("Fibonacci Series : ")
    while count<nterms:        
        nth = n1+n2
        print(n1)
        n1=n2
        n2=nth
        count += 1
    