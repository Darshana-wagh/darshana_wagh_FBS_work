#Write a program to check if given 3 digit number is a palindrome or not.
num = int (input("Enter number:"))

if num == int (str(num)[:: - 1]):
    print ("it is palindrome")
else:
    print("it is not palindrome")