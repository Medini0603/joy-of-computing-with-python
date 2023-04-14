

# read r
# write w
# readwrite r+
#append

# r for reading
# r+ opens for reading and writing (cannot truncate a file)
# w for writing
# w+ for writing and reading (can truncate a file)
# rb for reading a binary file. The file pointer is placed at the beginning of the file.
# rb+ reading or writing a binary file
# wb+ writing a binary file
# a+ opens for appending
# ab+ Opens a file for both appending and reading in binary. The file pointer is at the end of the file if the file exists. The file opens in the append mode.
# x open for exclusive creation, failing if the file already exists (Python 3)



with open("file1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("Hello I am medini\n")
    print(myfile.read())
myfile.close()

with open("file1.txt","a+") as myfile:
    myfile.write("I am fine\n")
    print(myfile.read())
myfile.close()