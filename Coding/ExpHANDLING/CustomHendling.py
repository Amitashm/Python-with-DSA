class UnderAgeExp(Exception):
    pass 

class AboveAge(Exception):
    pass



def CheckAge(name,year):
    age = 2026 - year

    if(age < 18):
        raise UnderAgeExp({name}," is  underage  ")
    elif(age>40):
         raise AboveAge({name}," is overage ")
    else :
        print(" eligble ")
    


try:
     CheckAge("ravi",1900)

except UnderAgeExp as e :
         print(e)
except AboveAge as a :
        print(a)
    
finally:
     print("program comlpleted")



    



 

