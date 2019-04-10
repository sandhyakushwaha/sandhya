c=int(input(" enter year"))
print("year is", c)
if c%4==0 or (c%100==0 and c%400==0):
    print("yes")
else:
    print("no")