n=int(input())
fact=1
if n==0 or n==1:
    print("1")
else:
    for i  in range(n):
        fact+=fact*i
    print(fact)