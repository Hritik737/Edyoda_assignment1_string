# Program to check if a string contains any special character.

string = input("Enter the string ")
special_characters=['@','$','#']
if special_characters in string:
    print('string is not acceptable')
else:
    print('string is acceptable')