letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
letter = letter.replace("<|Name|>", "Vishwas")
letter = letter.replace("<|Date|>", "25 November 2060")
print(letter)