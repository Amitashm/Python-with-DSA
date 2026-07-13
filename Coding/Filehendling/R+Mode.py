try:
    file = open("Students.txt","r+")

  
    print(file.read())
  

    

    file.seek(0)

    file.write("students are playing")


except  FileNotFoundError as fe:
    print(fe)
    print("file is not present ")



