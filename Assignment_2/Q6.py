# WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
basic = int(input("Enter salary:"))

da_amt = basic * 0.1
ta_amt = basic * 0.12
hra_amt = basic * 0.15

total_salary =basic + da_amt + ta_amt+ hra_amt
print(f'total_salary:{total_salary}')