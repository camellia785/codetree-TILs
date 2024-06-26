a1, b1 = input().split()
a2, b2 = input().split()
a3, b3 = input().split()

b1 = int(b1)
b2 = int(b2)
b3 = int(b3)

k = 0

if a1 == "Y":
    if b1 >= 37:
        k += 1
    
if a2 == "Y":
    if b2 >= 37:
        k += 1

if a3 == "Y":
    if b3 >= 37:
        k += 1

if k >= 2:
    print("E")

else:
    print("N")