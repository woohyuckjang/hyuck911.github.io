# 1. 세개의 숫자를 입력받아 가장 큰 수 찾기
'''
a = int(input("첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 : "))
c = int(input("세 번째 숫자 입력 : "))
print("입력 받은 수 : ", a, ",", b, ",", c)

if a > b:
    if a > c:
    print("a가 가장 큰 수 : ", a)
    else:
    print("c가 가장 큰 수 : ",c)
else:
    if b > c:
        print("가장 큰 수  b =", b)
    else:
        print("가장 큰 수 c =", c)
        
    '''
m=int(input("in :"))
a=int(input("in :"))
if a>m:
    m=a
a=int(input("in :"))
if a>m:
    m=a
print("가장 큰 수",m)

