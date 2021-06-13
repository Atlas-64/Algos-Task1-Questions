
def pattern(n):
    lst=[x for x in range(n-1) if x%2!=0]
    j=n//2
    print("*"*n)
    for i in lst:
        s1="*"*j
        s2=" "*(i)
        s3="*"*j
        j=j-1   
        if i<1:
            print(s1+"*",s3,sep="")   
        else:
            print(s1,s2,s3,sep="")     

    for i in range(len(lst)):
        j=j+1
        k=lst[len(lst)-i-1]
        if(j==1):
            continue
        s1="*"*j
        s2=" "*(k)
        s3="*"*j

        if i<len(lst):
            print(s1,s2,s3,sep="") 
        else:
            print(s1+"*",s3,sep="")    
    print("*"*n)


t=int(input())
n=[]
for i in range(t):
    n.append(int(input()))
for i in range(t):
    pattern(n[i])

