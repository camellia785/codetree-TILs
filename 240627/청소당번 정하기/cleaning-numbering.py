n = int(input())

n_class = 0
n_hallway = 0
n_toliet = 0

for i in range(0,n-1):
    if i%12==0:
        n_toliet += 1

    elif i%3==0:
        n_hallway += 1
    
    elif i%2==0:
        n_class += 1

print(f'{n_class} {n_hallway} {n_toliet}')