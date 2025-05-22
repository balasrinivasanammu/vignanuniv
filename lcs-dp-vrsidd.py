A=input()
B=input()
vrsidd=[[None]*(len(B)+1) for _ in range(len(A)+1)]
print(vrsidd)
for i in range(0,len(A)+1):
  for j in range(0,len(B)+1):
    if i==0 or j==0 :
      vrsidd[i][j]=0
    elif(A[i-1]==B[j-1]):
      vrsidd[i][j]=1+vrsidd[i-1][j-1]
    else:
      vrsidd[i][j]=max(vrsidd[i-1][j],vrsidd[i][j-1])
print(len(max(vrsidd))-1)
for i in range(0,len(A)+1):
  for j in range(0,len(B)+1):
    print(vrsidd[i][j],end=" ")
  print()