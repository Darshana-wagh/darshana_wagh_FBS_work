# Write a program to check if user has entered correct userid and password.
user_id = input('Enter the user id:')
password = input('Enter the password:')

if(user_id=='admin' and password=='146244'):
    print('This is an valid user')
else:
    print('Invalid user')