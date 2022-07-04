# Implementation of COCOMO 2 Model
import math

print("\n\t*** COCOMO 2 ***\n")
CPLX_table=[[0,0,1],[0,1,2],[1,2,2]]
weight_table=[[1,2,3],[2,5,8],[-1,-1,10]]
PROD=[4,7,13,25,50]

screen0=int(input("Enter no. of screen "))
screen1=int(input("Enter no. of screenviews "))
screen2=int(input("Enter no. of clients "))
screen3=int(input("Enter no. of servers "))

report0=int(input("Enter no. of reports "))
report1=int(input("Enter no. of reports section "))
report2=int(input("Enter no. of report clients  "))
report3=int(input("Enter no. of reports servers  "))

if screen1<3:
    s_row=0
elif screen1>=3 & screen1<=7:
    s_row=1
elif screen1>=8:
    s_row=2

if report1==0 ^ report1==1:
    r_row=0
elif report1==2 ^ report1==3:
    r_row=1
elif report1 >=4:
    r_row=2

if screen2<2 & screen3<3:
      col=0
elif((screen2 >=2 & screen2 <=3) & (screen3 >=3 & screen3 <=5)):
      col=1
elif(screen2 >3 & screen3 >5):
      col=2


s_CPLX=CPLX_table[s_row][col]
r_CPLX=CPLX_table[r_row][col]


OP=(screen0*weight_table[0][s_CPLX])+(report0*weight_table[1][r_CPLX])
print "\nObject Point : ",OP
reuse=int(input("\nEnter Reuse % : "))
NOP=(OP*(100-reuse))/100.0
print 'New Object Point NOP :',NOP
print("\nRate Programmer's Capability and Experience on Scale of 0-4 :\n")
print("\n0 - Very Low\n1 - Low\n2 - Nominal\n3 - High\n4 - Very High \n  ")
rating=int(input("Enter your choice : "))
print '\nProductivity : ',PROD[rating]
effort =NOP/PROD[rating]
print("\n\nEffort = NOP/Productivity :")
print '\nEffort : ',effort
