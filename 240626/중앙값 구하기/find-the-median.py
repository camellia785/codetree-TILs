a,b,c = map(int, (input().split()))

if a>b:
    if b>=c:
        print(b)
    
    elif b<c:
        if a>c:
            print(c)
        else:
            print(a)


elif a==b:
    print(a)



elif a<b:
    if b>=c:
        if a>c:
            print(a)
        else:
            print(c)
    elif b<c:
        print(b)