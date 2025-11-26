# f = open("My_File.txt")
# print(f.read())
# f.close()

with open("My_File.txt") as f: 
    print(f.read())
# The above code opens a file, reads its content, and automatically closes the file after the block is executed.