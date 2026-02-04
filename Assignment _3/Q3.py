# Write a program to input angles of a triangle and check whether triangle is valid or not.
Angle1=int(input('Enter a angle 1:'))
Angle2=int(input('Enter a angle 2:'))
Angle3=int(input('Enter a angle 3:'))

sum = Angle1+Angle2+Angle3
if(sum==180):
    print('This is valid triangle.')
else:
    print('This is invalid triangle.')

