# Implementation of COCOMO 1 Model

while i==1:
 print("\n1. Organic\t2. Semidetached\t3. Embedded")
 ch=int(input("\tEnter your choice: "))

 if ch==1:
        p=math.pow(l,1.05)
	effort=2.4*p
	q=math.pow(effort,0.38)

 elif ch==2:
	p=math.pow(l,1.12)
	effort=3.0*p
	q=math.pow(effort,0.35)

 elif ch==3:
	p=math.pow(l,1.20)
	effort=3.6*p
	q=math.pow(effort,0.32)

 else:
	print("Invalid choice!")

 tdev=2.5*q
 print()
 print("Effort                   :",effort," PM")
 print("Nominal Development Time :",tdev," Months")
 print("Cost to Develop          : Rs ",(s*effort))
 
 i=int(input("If you continue run this prees 1 : "))

print("Thank you")

