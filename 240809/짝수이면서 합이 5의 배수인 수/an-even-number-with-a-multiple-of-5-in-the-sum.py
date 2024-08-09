# input 받기
n = int(input())

# Test라는 magic 함수 정의
# % 나머지, // 몫
def Test(n):
    if n%2==0 and ((n%10)+(n//10))%5==0:
        print("Yes")
    else:
        print("No")

Test(n)