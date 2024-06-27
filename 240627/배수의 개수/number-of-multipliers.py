cnt_3 = 0
cnt_5 = 0

for i in range(0,10):
    n = int(input())

    if n%3==0 and n%5==0 :
        cnt_3 += 1
        cnt_5 += 1

    elif n%3==0:
        cnt_3 += 1

    elif n%5==0 :
        cnt_5 += 1

    
print(f'{cnt_3} {cnt_5}')