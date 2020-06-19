
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
