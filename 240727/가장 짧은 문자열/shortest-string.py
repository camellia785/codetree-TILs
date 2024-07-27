a = len(input())
b = len(input())
c = len(input())

if a>b:
    if b>c:
        result = a-c

    elif b<c:
        if a>c:
            result = a-b
        else:
            result = c-b

elif a<b:
    if a>c:
        result = b-c

    elif a<c:
        if b>c:
            result = b-a

        else:
            result = c-a
print(result)