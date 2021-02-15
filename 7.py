a=list(map(int, input().split()))
b=list(map(int, input().split()))

wet=0
for i in range(len(a)):
   for j in range(len(b)):
      if a[i]==b[j]:
         wet+=1
         b[j]=-111111111111111
         break

print(wet)