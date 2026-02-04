# Write a program to input all sides of a triangle and check whether triangle is valid or not.
a = int(input('enter the side 1:'))
b = int(input('enter the side 2:'))
c = int(input('enter the side 3:'))
if(a + b > c and a+ c >b and b+c>a):
    print("valid triangle")
else:
    print("not valid")