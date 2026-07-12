import random
  # Custom Exception
class HighTemprature(Exception):
    pass
class LowTempratature(Exception):
    pass
class ModrateTemp(Exception):
    pass

def CheckTemp(temp):

    if temp > 22 and  temp<27:
        raise ModrateTemp({temp},"is moderate ")
    elif temp > 27 :
        raise HighTemprature({temp} , "is high temp")
    elif temp > 22 :
        raise LowTempratature({temp}," is low temp")
    

try:

    a = [10,-2,22,76,32,45,27]

    temp = random.choice(a)

    CheckTemp(temp)

except LowTempratature as l:
    print(l)
except HighTemprature as h:
    print(h)
except ModrateTemp as m:
    print(m)
finally:
    print("Program is completed ")

