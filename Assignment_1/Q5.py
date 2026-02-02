# Write a program to enter P, T, R and calculate Compound Interest.
P = int (input("Enter principle amount:"))
R = int (input("Enter rate:"))
T = int (input("Enter time(years:)"))

compound_int = (P * (1 + (R/100)**T)-P)
print(f'compound_intrest:{compound_int}')