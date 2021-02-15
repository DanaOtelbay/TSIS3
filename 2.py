a=list(map(int, input().split()))
mn= 111111111
for i in range(0, len(a)):
   if a[i]>0 and a[i]<mn:
      mn=a[i]

print(mn)