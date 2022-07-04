userinput= input('enter the name of the file:   ')
myfile=open(userinput)
count=0
for line in myfile:
    print(line)
    count=count+1
print(count)

myfile.close()
kloc=count/100

obp=float(input("enter the object point"))


reuse=float(input("eneter the reuse."))


pm=float(input("eneter the person per month"))


co=float(input("eneter the value of cost driver."))


a=float(input("eneter the valuof a"))


b=float(input("neter the value of b."))

reuse=reuse/100
nop=(obp*(100-reuse))/100
prod=nop/pm
E=nop/prod
print("the new object point(NOP) is :",nop)
print("finally the person per month is computed as E is",E)
effre=kloc*(22/7)*co
effrp=a*pow(kloc,b)*(22/7)*co
print("the effort of early design model :",effre)
print("the  efort of post architecture model",effrp)

#https://arxiv.org/ct?url=https%3A%2F%2Fdx.doi.org%2F10.1109%2FTIFS.2012.2218597&v=39ba7a2e