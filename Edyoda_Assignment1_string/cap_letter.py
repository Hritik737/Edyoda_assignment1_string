# Python program to capitalize the first and last character of each word in a string.

string=input("enter the string: ")
s=(string.split())
print(s, type(s))
for i in s:
    l=list(i)
    if len(i)>1:
        a=l[0].upper()+i[1:(len(i)-1)] +l[-1].upper()
    else:
        a=l[0].upper()
    print(a)