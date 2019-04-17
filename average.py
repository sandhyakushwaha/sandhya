sum=0
list=[]
n=int(input())
for i in range(1,n+1):
    ele=int(input())
    list.append(ele)
for i in list:
    sum=sum+i
print(sum//n)    
    