n = int (input("Enter the terms you want:"))
i = 0
a,b = 3, 4

while(i<n):
    print(a, end=" ")
    a, b=b,a+b
    i+=1