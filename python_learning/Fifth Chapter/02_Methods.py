#  Dictionary methonds
marks = {
    "Rohan  " : 34 , 
    "Vishwas" : 534 , 
    "Shweta" : 9334  
}

print(marks.items()) 

print(" ")

print(marks.keys()) 

print( "  ")

print(marks.values())

print(" " )

marks.update({"Vishwas ": 23223 , "Renuka" : 3434})

print(marks)

print(marks.get("Rohan3")) # This will return none becuase of get method 

print([marks.Harry]) # This will give error because of direct method
