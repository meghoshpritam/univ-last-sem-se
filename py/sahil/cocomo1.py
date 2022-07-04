userinput= input('enter the name of the file:   ')
myfile=open(userinput)
count=0
for line in myfile:
    print(line)
    count=count+1
print(count)

myfile.close()
kloc=count/100
oe=2.4*(pow(kloc,105/100))
print("the organis effort  ",oe,"pm")
ot=2.5*(pow(oe,38/100))
print("the organis tdev  ",ot,"month")
se=3.0*(pow(kloc,112/100))
print("the semidetached effort:",se,"pm")

st=2.5*(pow(se,35/100))
print("the semidetached tdev  ",st,"month")
ee=3.6*(pow(kloc,120/100))
print("the embedded effort  ",ee,"pm")
et=2.5*(pow(ee,32/100))
print("the embedded tdev  ",et,"month")
