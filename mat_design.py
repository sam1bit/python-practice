"""
n=7
m=21

for i in range(n//2):
    a=1+i*2
    print((".|."*a).center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(n//2):
      print((".|."*a).center(m,"-"))
      a=a-2
 
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print()"""
####################################
n, m = map(int,input().split())
alist=[]
for i in range(n//2):
    a=1+i*2
    alist.append((".|."*a).center(m,"-"))
alist.append("WELCOME".center(m,"-"))
for i in range(n//2):
      alist.append((".|."*a).center(m,"-"))
      a=a-2
print("\n".join(alist))
