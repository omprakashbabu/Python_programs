def SI(a,b,c):
    return (a*b*c)/100
    
p=int(input("Enter the principle amount : "))
n=int(input("Enter a number of years : "))
r=int(input("Enter a rate of interest : "))
x=max(p,n,r)
print("The simple interest is",x)