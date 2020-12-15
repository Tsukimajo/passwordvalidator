import re

password = input('Enter your password: ')
searchOne = re.search(r'\d{2}|\d', password)
searchTwo = re.search(r'[!@#$%&]{2}|[!@#$%&]', password)

if len(password) >= 7:
    if searchOne:
        if searchTwo:
            print('Strong')
        else:
            print('Weak')
    else:
        print('Weak')
else:
    print('Weak')