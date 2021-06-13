p=input()
q=input()
r=input()

j=p.split(" ")
k=q.split(" ")
l=r.split(" ")

if "" in k:
    k.remove("")
if "" in l:
    l.remove("")

x=list(map(int, j))
y=list(map(int, k))
z=list(map(int, l))

sb=x[1]
for i in range(x[0]):
    if(y[i] and z[i] ):
        x[1]+=x[2]
    elif (y[i] and (z[i]==0) ):
        x[1]-=x[3] 
        
if (x[1]>sb):
    print("promoted")
elif (x[1]==sb):
    print("no change")
elif (x[1]<sb):
    print("demoted")