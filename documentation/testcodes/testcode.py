"""
This is where all my testing code and
operations will go before my final project
"""

print("This is experiment one")
#tank id
tank_id=int(input("What is the tank ID: "))

#amonia
amo=float(input("Amonia levels: "))
#nitrite
nit=float(input("Nitrite levels: "))
#nitrate
nat=int(input("Nitrate levels: "))
#date
date=input("todays date(dd-mm-yy): ")
#ouput pass/fail
print(date, "Tank ID:", tank_id)
#amonia input
if amo>=0.25:
    print("Amonia Levels: Fail")
else:
    print("Amonia Levels: Pass")

#nitrite input
if nit>=2.5:
    print("Nitrite Levels: Fail")
else:
    print("Nitrate Levels: Pass")
#nitrate input
if nat>=5:
    print("Nitrate Levels: Fail")
else:
    print("Nitrate Levels: Pass")

#tank id input