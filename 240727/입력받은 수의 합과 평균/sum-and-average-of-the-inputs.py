n = int(input())
sum = 0


for _ in range(n):
    number = int(input())
    sum += number

avg = sum/n

print(sum, avg)