d = dict()
# key- word, value- number of rep-s

try:
   while True:
      line = input().split()
      for word in line:
         if d.get(word, 0)!=0 : d[word] +=1
         else: d[word]=1
except:
   pass

def f(item):
   return (-item[1], item[0])

for item in sorted(d.items(), key=f):
   print (item[0])