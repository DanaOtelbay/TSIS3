# a=list(map(int, input().split()))
# b=list(map(int, input().split()))

# s1=set(a)
# s2=set(b)

# ans=list(s1.intersection(s2))

# for i in range(len(ans)):
#     print(ans[i],end=' ')

print(set(map(int, input().split())).intersection(set(map(int, input().split()))))