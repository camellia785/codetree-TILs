N=int(input())
A=[int(input()) for _ in range(N)]

# arr배열의 arr[s] ~ arr[e]제거하고, 남은 결과를 리턴

def f(arr, s, e) -> list[int]:
    temp = []
    for i in range(len(arr)):
        if s <= i <= e:
            continue
        temp.append[arr[i]]
    return temp

Q = int(input())
for _ in range(Q):
    s, e = map(int, input().split()) # 1
    A = f(A, s-1, e-1)

print(A)