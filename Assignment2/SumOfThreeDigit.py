d = int(input("Enter three digit number:"))

hundreds = d // 100
tens = (d // 10) % 10
units = d % 10

digit_sum = hundreds + tens + units

print(f'sum of digits:{digit_sum}')