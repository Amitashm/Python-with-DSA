try:
    file = open("Students.txt","w+")

  

  

    file.write("students are playing")

    file.seek(0)

    print(file.read())


except  FileNotFoundError as fe:
    print(fe)
    print("file is not present ")

