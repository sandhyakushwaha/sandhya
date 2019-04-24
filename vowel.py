s=input()
b="aeiouAEIOU"
c=any(i in s for i in b)
if c:
    print("yes")
else:
    print("no")