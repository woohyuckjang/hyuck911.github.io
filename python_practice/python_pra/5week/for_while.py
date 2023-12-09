print("-"*38)
print("for, while문 : 2021136114-장우혁")
print("-"*38)
# 반복문 예제
# 1 ~ 100까지 의 합 구하기
# 1. for문
'''
hap = 0;
for i in range(1,101):
    hap=hap+i
print("1부터 100까지의 합 : %d" % hap);
print("1부터 100까지의 합 : {:d}".format(hap))
'''
# 2. while문
'''
hap = 0
i = 1
while i < 101:
    hap = hap+i
    i+=1
print("1부터 100까지의 합 : %d" % hap)
print("1부터 100까지의 합 : {:d}".format(hap))
'''

# 3. 3의 배수만 더하기
'''
hap = 0;
for i in range(0,101,3):
        hap=hap+i
print("3의 배수 합 : %d" % hap);
'''
#if 문으로
hap = 0;
for i in range(1,101):
    if i % 3 == 0:
        hap=hap+i
print("3의 배수 합 : %d" % hap);


# 시작값, 끝값, 배수 입력받아서 실행




























