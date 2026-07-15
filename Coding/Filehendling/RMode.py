 # Read Mode 
try:
    file = open("Student.txt" , "r")

    print(file.read())

except FileNotFoundError as fe :
    print("not abel to find exception")

else:
    print("problem in prgramS")
finally:
    print("Complete Program ")  