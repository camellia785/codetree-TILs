N = int(input())
A = [int(input()) for _ in range(N)]

def f(arr, s, e) -> list[int]:
    return [arr[i] for i in range(len(arr)) if i < s or i > e]

for _ in range(2):
    s, e = map(int, input().split())
    A = f(A, s-1, e-1)

print(len(A))
for a in A:
    print(a)