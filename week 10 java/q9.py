def count_u_and_l_case(str):
    upper_count=0
    lower_count=0
    
    for char in str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count,lower_count

a=input("Enter a string : ")
upper,lower = count_u_and_l_case(a)

print("Number of upper case letters :",upper)
print("Number of lower case letters :",lower)