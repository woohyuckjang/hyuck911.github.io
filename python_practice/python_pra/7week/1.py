#1 ~ 15까지 랜덤 값을 중복 없이 3개 생성하여
# 출력하는 코드 작성하기
from random import random
num1=num2=num3=0
#num1=0;num2=0;num3=0
#num1,num2,num3=0,0,0

while True:
    rand=int(random()*15)+1
    if rand != num1:
        num1 = rand
        break

while True:
    rand=int(random()*15)+1
    if rand != num1 and rand != num2:
        num2 = rand
        break

while True:
    rand=int(random()*15)+1
    if rand != num1 and rand != num2 and rand != num3:
        num3 = rand
        break

print("num1:",num1,", num2:",num2,", num3:",num3)
