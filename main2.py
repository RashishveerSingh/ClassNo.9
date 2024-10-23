# activity 2 check the armstrong number

a = int(input("enter the namber if u wan to check if armstong namber or no:"))
sum = 0
origin_num = a
while origin_num > 0:
    digit = origin_num % 10
    sum += digit ** 3
    origin_num //= 10
if a == sum:
    print("it is an armstrong")
else:
    print("no armstong namber detected (buzzer sound)")