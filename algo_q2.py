count=0
n=int(input())
a=input()
g= n//2
if n>1 and n<=1000000 and ((n%2)==0):
    for i in range (n//2):
        b=a[:((g))]
        c=a[-((g)):]
        if (b==c):
            a=b
            g=g//2
            count+=1
            continue
        else:
            break
print(count)