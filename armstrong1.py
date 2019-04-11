n = int(input())
k = int(input())
 
for num in range(n+1,k):
   sum = 0
 
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)
