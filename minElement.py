list=[]
n=int(input("enter number of elements to be entered"))
for i in range(1,n+1):
    ele=int(input())
    list.append(ele)
min=list[0]
for i in list:
    if i<min:
        min=i
print(min) 