n=int(input())
a=input()
k=[i for i in a if (int(i)-int('0'))>1]

if len(k)==0 and a.count('0')!=n and a.count('1')!=n and n<=100000 :
    b="0b"+a
    p=str(bin(int(b,2)-1)).lstrip('0b')
    q=str(bin(int(b,2)+1)).lstrip('0b')
    if len(p)!=len(q):
        print(-1)
    else:
        print(p,q)    

else:
    print(-1)