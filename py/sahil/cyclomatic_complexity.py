E=int(input("Enter the number of edges in the control flow graph: "))
N=int(input("Enter the number of nodes in the control flow graph: "))
P=int(input("P = the number of connected components: "))
print('E=',E,'\nN=',N,'\nP=',P)
M=E-N+2*P
print("Cyclomatic complexity: ",M)