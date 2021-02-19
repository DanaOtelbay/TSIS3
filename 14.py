l = input().split()
k=int(input())
k%=len(l)

for elem in l[-k:] + l[:-k]:
   print(elem, end=" ")
#print(l[-k:], l[:-k])