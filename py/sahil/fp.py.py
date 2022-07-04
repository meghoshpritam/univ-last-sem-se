import math

print("\n\t-----FUNCTION POINT (FP)-----\n")


def fround(x):
  x=x+0.5
  a=x
  return(a)


weights=[[3,4,6],[4,5,7],[3,4,6],[7,10,15],[5,7,10]]
UFP=0
F=0
func_units=['External inputs','External Outputs','External Enquiries','Internal Logical Files','External Interface Files']
complexity=['low','average','high']

inputs=[[0 for i in range(7)]for j in range(7)]
for i in range(5):
   for j in range(3):
      print 'Enter number of : ',complexity[j],func_units[i]
      inputs[i][j]=int(input())

  #calculating UFP

for i in range(5):
 for j in range(3):
      UFP=UFP+(inputs[i][j]*weights[i][j])

print '\nUnadjusted Function Point(UFP) = ',UFP

print("\nEnter Rating of 14 factors on the scale of 0-5 :\n")
print("\n 0 - No Influence")
print("\n 1 - Incidental")
print("\n 2 - Moderate")
print("\n 3 - Average")
print("\n 4 - Significant")
print("\n 5 - Essential")

print("\n")
i=1
while i<15:
    rating=int(input())
    if 0<=rating<=5:
        F=F+rating
        i=i+1
    else :
      print("ReEnter Rating scale of 0-5")

CAF=0.65+0.01*F

FP=UFP*CAF

print '\nAdjusted Function Point = ',FP
print '\nOR FP = ',int(fround(FP))
