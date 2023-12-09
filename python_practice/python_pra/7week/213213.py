'''
# 1. numbers =[10, 20, 30, 40, 50, 60, 70] 리스트의
# 모든 값을 더한 결과 출력

numbers = [10,20,30,40,50,60,70]
hap = 0
# 방법 1
for i in numbers:
    hap += i # hap=hap+i
print(hap)

# 방법 2
hap = 0
for i in range(len(numbers)):
    hap = hap+numbers[i]
print(hap)

# 2. 1 ~ 45까지 임의의 값을 중복 없이 6개 생성하여 출력하는 코드를 작성
from random import random
numbers=[] # 6개의 숫자 넣을 리스트
cnt=0 # 숫자 개수

while True:
    rand=int(random()*45)+1
    if rand not in numbers:
        numbers.append(rand)
        cnt+=1
        if cnt == 6:
            numbers.sort()
            break
print(numbers)
'''
# 3. lst_sec = [['홍길동', '남', 36], ['김수양', '여', 32], ['박담소', '남', 28]]**
# 위의 2차 리스트 자료를 다음과 같은 형식으로 출력
#          이름 : 홍길동
#          성별 : 남
#          나이 : 36
lst_sec = [['홍길동', '남', 36], ['김수양', '여', 32], ['박담소', '남', 28]]

for i in lst_sec:
    print("-"*15)
    print("이름 : {}".format(i[0]))
    print("성별 : {}".format(i[1]))
    print("나이 : {}".format(i[2]))
