start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Armstrong numbers between {start} and {end} are:")

for num in range(start, end + 1):
    
    num_str = str(num)
    num_digits = len(num_str)
    
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    if sum_of_powers == num:
        print(num, end=" ")