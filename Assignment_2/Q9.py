# Write a program to swap two numbers without using third variable.
x = int(input("Enter x:"))
y = int(input("Enter y:"))

x,y = y,x

print(f'After swapping x:{x}, y:{y}')