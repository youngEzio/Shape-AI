import hashlib                                                  #Importing the library for md5
string = input("Enter the string to be converted into md5: ")   #Enter the string to be converted
string1 = hashlib.md5(string.encode())                          #Calling md5 function
string2 = string1.digest()                                   #Returning data into hexadecimal format
print(string2)                                                  #Printing the md5 encrypted string