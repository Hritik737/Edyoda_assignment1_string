# Python program to count the number of vowels in a
string=str(input("Enter the string :"))
spl=list(string)
vowel=0
for j in spl:
    if j=='a' or j=='e' or j=='i' or j=='u' or j=='o' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U':
        vowel+=1
print(vowel)


    