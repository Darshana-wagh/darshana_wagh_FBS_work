#WAP to print factorial of a number .
n = int(input("Enter the number:"))
i = 1
fact = 1
while(i<=n):
    fact*=i
    i+=1
print(f'Factorial of {n} is {fact}')