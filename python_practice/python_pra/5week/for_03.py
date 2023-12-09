# 1 ~ 10까지 합 구하기
'''
hap = 0
for i in range(1,11):
    hap = hap + i
print(hap)
'''
# 1 ~ 100까지의 수 중 짝수만 합 구하기
'''
hap = 0
for i in range(2, 101, 2):
    hap = hap + i
print(hap)
'''
# for, if문 같이 사용
hap = 0
for k in range(1, 101): # 1 ~ 100까지 반복
    # 짝수 걸러내기
    if k % 2 == 0:
        hap = hap + k
print(" 1~100까지의 짝수의 합 : ",hap) # 결과 출력하기
print(" 1~100까지 짝수의 합 : %d" % hap) # C언어
print(" 1~100까지의 짝수의 합 : {:d}".format (hap)) # 파이썬
