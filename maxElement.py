list=[]
n=int(input("enter number of elements to be entered"))
for i in range(1,n+1):
    ele=int(input())
    list.append(ele)
max=list[0]
for i in list:
    if i>max:
        max=i
print(max) 