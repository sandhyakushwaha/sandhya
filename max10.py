data=[]
list=[]
for i in range(10):
    ele=int(input())
    list.append(ele)
while list:
    min=list[0]
    for i in list:
        if i<min:
            min=i
    data.append(min)
    list.remove(min)
print(data[9])