n = int(input())
sum = 0

for _ in range(n):
    number = int(input())
    if number %2 != 0 and number%3==0:
        sum += number

print(sum)