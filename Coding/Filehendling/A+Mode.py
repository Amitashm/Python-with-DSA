# Appends   Modes

try:
    file = open("Students.txt","a+")

    
    file.write(" now students are not  playing")
    file.seek(0)

    print(file.read())



except  FileNotFoundError as fe:
    print(fe)
    print("file is not present ")



