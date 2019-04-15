new_list= []
data_list= []
n=int(input("enter the size"))
for i in range(1,n+1):
    ele=int(input())
    data_list.append(ele)
#print(data_list)
while data_list:
    min=data_list[0]
    for i in data_list:
        if i<min:
            min=i
    new_list.append(min)
    data_list.remove(min)
print(new_list)