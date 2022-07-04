k=float(input("Enter the value of effort :"))
t=float(input("Enter the development time...:"))
print("1.poor development...")
print("2.good development...")
print("3.Excellent development...")
print("Enter your choice:")
ch=int(input("enter your choice"))
if ch==1:
    L=2*pow(k,1/3)*pow(t,4/3)
    print("The product size is ..",L,"KLOC")
elif ch==2:
    L=8*pow(k,1/3)*pow(t,4/3)
    print("The product size is ..",L,"KLOC")
elif ch==3:
    L=11*pow(k,1/3)*pow(t,4/3)
    print("The product size is ..",L,"KLOC")
else:
    print("Wromg choice given:")
    
