a = int(input())

for i in range(1,a+1):
    if (i%2==0 and i%4!=0) or ((i//8)%2==0 ) or (i%7<4):
        continue
        
    # 원래는 else 쓰는데, continue 활용 문제니까 continue 하면 바로 print 가능
    print(i, end=' ')