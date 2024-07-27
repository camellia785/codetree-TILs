str1= input()
alpha = input()

k = len(str1)
i = 0
count = 0

for i in range(k):
    if alpha in str1[i]:
        count += 1

print(count)