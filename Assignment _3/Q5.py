# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input('Enter the side 1:'))
b = int(input('Enter the side 2:'))
c = int(input('Enter the side 3:'))
if(a==b==c):
    print('The triangle is equilateral.')
elif(a==b or b==c or a==c):
    print('The triangle is isosceles.')
elif(a!=b!=c):
    print('The triangle is scalene.')
else:
    print('this is not an isosceles, equilateral,scalene triangle.')
    