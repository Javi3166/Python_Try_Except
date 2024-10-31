'''
number = int(input("Enter a number: "))
print(number)

This has an error in case user inputs letters
'''
from multiprocessing.managers import Value

'''
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input.")

Outputting "Invalid input" despite error being 10/0 and not user input
'''

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input.")