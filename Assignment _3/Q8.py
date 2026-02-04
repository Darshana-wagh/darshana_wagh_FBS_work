# Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random 
# number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
correct_userid = "admin"
correct_password = "1234"

userid = input ("Enter user id:")
password = input ("Enter password:")


if userid == correct_userid and password == correct_password:
    capcha = random. randint (1111,9999)

    print("capcha:", capcha)

    user_input = int (input("Enter the above capcha number:"))

    if user_input == capcha:
        print("login *sucessfully.")

    else:
        print("capcha did not match login failed.")
else:
    print("invalid user id or password.")


