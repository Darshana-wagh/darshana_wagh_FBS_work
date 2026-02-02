# Find the sum of three-digit number.
basic = int(input("Enter salary:"))

da_amt = basic * 0.1
ta_amt = basic * 0.12
hra_amt = basic * 0.15

total_salary =basic + da_amt + ta_amt+ hra_amt
print(f'total_salary:{total_salary}')