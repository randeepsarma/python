#string are immutable
a='HARRY...HARRY'
print(len(a))
print(a.upper())#a new string is made instead of altering the previous one 
print(a.lower())

b="HArRY!!!!!!!!!!!";
print(b.rstrip("!"))#strips only trailing characters

print(a.replace("HARRY","JOHN"))

print(a.capitalize())#capitalise

print(a.center(50))

print(a.count("HARRY"))# count instances of a smaller word in a larger word

print(a.endswith("HARRY"))

print(a.endswith("HARRY",0,5))

print(a.find("HARRY"))#returns index of first instance of the word


print(a.find("Hoven"))

print(a.index("HARRY"))

print(a.isalnum())#checks if string contains onlu alphanumeric characters A-Z,a-z,0-9

str="scrfcrtgcvtg"
print(str.isalpha())#A-Z,a-z

print(str.islower())

str1="rfckrmfcmrfkcm\n\t"

print(str1.isprintable())# checks if a string has \n,\t

str2="         "
print(str2.isspace())#checks if there is some space in the string

str3="World health"
print(str3.istitle())#checks if all words are capitalised or not .

str4="dcendnRFCDXEDE"
print(str4.swapcase())# changes uppercase to lowercase and vice versa 


str5="world health organisation"
print(str5.title())
