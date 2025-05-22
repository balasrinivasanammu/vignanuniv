A=input("Enter the main string")
B=input("Enter the substring")
l=[]
n=[]
for i in range(len(A)):
  l.append(A[i])
l.append('\0')
for i in range(len(B)):
  n.append(B[i])
n.append('\0')
def vrsidd(i,j):
  if(l[i]=='\0' or n[j]=='\0'):
    return 0
  elif(l[i-1]==n[j-1]):
    return 1+vrsidd(i+1,j+1)
  else:
    return max(vrsidd(i+1,j),vrsidd(i,j+1))
print(vrsidd(0,0))