#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
s1 = int (input("Enter marks of subject 1:"))
s2 = int (input("Enter marks of subject 2:"))
s3 = int (input("Enter marks of subject 3:"))
s4 = int (input("Enter marks of subject 4:"))
s5 = int (input("Enter marks of subject 5:"))

total_marks= s1 + s2 +s3 +s4 +s5
average = (total_marks*500)/100

print(f'percentage: {average}')

if(average >=85):
    print("first class destination")
elif(average>= 75):
    print("second class destination")
elif(average>=67):
    print("third class destination")
else:
    print("fail")

