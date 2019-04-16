s = input()
count = 0
for i in range(len(s)):
    if(s[i].isalpha()):
        pass
    elif(s[i].isdigit()):
        pass
    else:
        count = count + 1
        
print(count)