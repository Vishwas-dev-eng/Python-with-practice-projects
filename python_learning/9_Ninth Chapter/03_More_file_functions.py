f = open("My_File.txt")

# lines = f.readlines()
# print(lines , type(lines)) 

# line1 = f.readline()
# print(line1 , type(line1))  # -----> This is for individual line printing 

line = f.read()
while (  line != "") : 
    print(line)
    line = f.readline()

f.close() 