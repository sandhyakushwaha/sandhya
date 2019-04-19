data=[]
list=[]
n=10
for i in range(1,n+1):
    ele=int(input())
    list.append(ele)
while list:
    min=list[0]
    for i in list:
        if i<min:
            min=i
    data.append(min)
    list.remove(min)
print(data[0]) 
