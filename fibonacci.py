n=int(input())
a=0
b=1
for i in range(1,n):
    print(b,end=" ")
    c=a+b
    a=b
    b=c
print(b) 