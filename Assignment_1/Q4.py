# Write a program to enter P, T, R and calculate simple Interest.
P = int (input("Enter principle amount:"))
R = int (input("Enter rate:"))
T = int (input("Enter time(years:)"))

simple_int = (P * T * R)/100
print (f'simple_intrest:{simple_int}')
