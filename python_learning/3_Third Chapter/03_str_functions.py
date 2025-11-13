name = "Vishwas is a good boy "
print(len(name)) # This function is used to find the length of the string 
print(name.endswith("as")) # This function is used to check whether the string ends with the given substring
print(name.startswith("vis")) # This function is used to check whether the  string starts with the given the substring 
print(name.capitalize()) # This function is used to captialize the first letter of the string

count = str.count(name ,"s") # Here count functions is used to count the c occurrences of 's ' in the string name
print(count)

index = str.index(name, "a" ) # This function is used to find the index of the first occurrence of 's ' in the string name
print(index) 

replace = str.replace(name,  "good " , "bad")# This function is used to replace the first occurrence  of the given string with another string 
print(replace)
