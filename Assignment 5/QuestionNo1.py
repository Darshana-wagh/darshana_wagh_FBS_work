correct_id = "admin"
correct_password = "1234"

attempts = 3

for attempt in range(attempts):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect User ID or Password.")
        if attempt < attempts - 1:
            print(f"You have {attempts - attempt - 1} attempt(s) left.\n")
else:
    print("Too many failed attempts. Program terminated.")