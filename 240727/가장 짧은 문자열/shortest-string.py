st1 = input()
st2 = input()
st3 = input()

a = len(st1)
b = len(st2)
c = len(st3)

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