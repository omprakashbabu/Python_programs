def isPalindrome(s):
    #changes
    if s == s[::-1].:
        print("The given string is Palindrome")
    else:
        print("The given string is not a Palindrome")
        
str_input = input ("Enter a string : ")
print("The reverse of the string is", str_input[::-1])
isPalindrome(str_input)
