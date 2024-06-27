cnt_3 = 0
cnt_5 = 0

'''
방법 1) 합집합, 교집합으로 구하기
'''
for i in range(0,10):
    n = int(input())

    # 교집합부터
    if n%3==0 and n%5==0 :
        cnt_3 += 1
        cnt_5 += 1

    # 3만
    elif n%3==0:
        cnt_3 += 1

    # 5만
    elif n%5==0 :
        cnt_5 += 1

''' 
방법2) 그냥 if 두개 쓰기

for _ in range(10):
	a = int(input())
	
	if a % 3 == 0:
		cnt3 += 1
	if a % 5 == 0:
		cnt5 += 1
'''
    
print(f'{cnt_3} {cnt_5}')