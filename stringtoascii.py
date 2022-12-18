#The script will iterate through each character in the password, convert it to its ASCII value, 
#add a value to the ASCII value, and print the resulting character. This process should allow you to decrypt the password 
MyString = '777777'  # replace this value
i = 0
base = 0
print("Converting to ASCII value")
while i < len(MyString):
    char = MyString[i]
    j = ord(char)
    j = j + base
    print(chr(j), end="")
    base = base - 1
    i += 1
