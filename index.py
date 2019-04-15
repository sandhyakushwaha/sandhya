data=[]
n=int(input())
for i in range(1,n+1):
    ele=int(input())
    data.append(ele)

for i in data:
    print(i,data.index(i))