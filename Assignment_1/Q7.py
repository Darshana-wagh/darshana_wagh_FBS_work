# Program to Find the Roots of a Quadratic Equation
a = int(input("Enter the value of a:"))
b = int (input("Enter the value of b:"))
c = int (input("Enter the value of c:"))

ans = (b*b)- (4*a*c)
ans = ans**0.52
result1=(-b+ans)/(2*a)
result2=(-b-ans)/(2*a)
print("result1:",result1)
print("result2:",result2)