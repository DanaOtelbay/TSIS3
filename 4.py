a=list(map(int, input().split()))

for i in range(0, len(a)):
   if a[i]==0:
      for j in range(i, len(a)):
         if a[j]!=0:
            x=a[i]
            a[i]=a[j]
            a[j]=x
            break
         else:
            continue
   else:
      continue

print(a)
