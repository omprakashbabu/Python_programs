choice = int (input("Finding area and perimerter\nEnter 1 for Circle\nEnter 2 for Redtangle\nEnter 3 for Triangle\n\nEnter your choice : "))

if choice == 1:
    r=int(input("Enter the radius of the circle : "))
    print("The area is ",3.14*r*r)
    print("The perimeter is ",2*3.14*r)
    
elif choice == 2:
    a=int(input("Enter the length of the rectangle : "))
    b=int(input("Enter the breadth of the rectangle : "))
    print("The area is ",a*b)
    print("The perimeter is ",2*(a+b))
    
elif choice == 3:
    c=int(input("Enter the side 1 of the Triangle : "))
    d=int(input("Enter the side 2 of the Triangle : "))
    e=int(input("Enter the side 3 of the Triangle : "))
    s = (c + d + e) / 2
    area = (s*(s-c)*(s-d)*(s-e)) ** 0.5
    print("The area is %0.2f"%area)
    print("The perimeter is ",c+d+e)
    
else:
    print("Invalid input\n")
