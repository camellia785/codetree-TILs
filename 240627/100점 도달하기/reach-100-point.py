n = int(input())

for i in range(n , 101):
    if i >= 90:
        score = 'A'
    elif i >= 80:
        score = 'B'
    elif i >= 70:
        score = 'C'
    elif i >= 60:
        score = 'D'
    else:
        score = 'F'

    print(score, end=" ")
    i+= 1