from random import random

#1. 1~100까지 랜덤 값을 6개 출력하는 코드를 작성하시오.
for i in range(6):
    print(int(random()*100)+1)

# 1~100까지 랜덤 값을 반복하여 출력하되
# 50이 출력되는 순간 반복을 종료하는 코드를 작성하시오.
count=0
while True:
    rand=int(random()*100) + 1
    print(rand)
    count += 1
    if count == 20:
        print("count 20")
        break
    if rand == 50:
        break
    
