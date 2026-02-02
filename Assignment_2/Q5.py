# WAP to calculate selling price of book based on cost price and discount.
cp = int(input("Enter the cost prize:"))
d = int (input("Enter discount:"))

d = cp * d / 100
sp = cp + d

print(f'Selling prize:{sp}')