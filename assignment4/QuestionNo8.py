start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Numbers between {start} and {end} divisible by 7 and multiple of 5:")

for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=" ")