#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('Enter gender(M/F):')
age = int(input('Enter age:'))

if gender in ['f', 'F', 'female', 'Female', 'FEMALE']:
    if age>17:
        print('Eligible for marrige.')
    else:
        print('not eligible for marrige.')
else:
    if age>20:
       print('eligible for marrige.')
    else:
        print('not eligible for marrige.')

