
try:
    file = open("Students.txt","x")

    file.write("Hello student")

except FileExistsError as e :
    print("already exist ")

finally:
    print ("completed")