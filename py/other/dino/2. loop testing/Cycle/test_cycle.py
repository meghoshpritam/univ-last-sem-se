fpath=input("Enter the path of the program file :")
fp1 = open(fpath,'r')
line=" "
count = 1

while(line != ""):
  line=fp1.readline()
  if("for" in line and ":" in line ):
    count +=1
  elif("if(" in line or "while(" in line and "):" in line):
    count += 1
fp1.close()
print("Cyclomatic Complexity of the given program is :",count)
