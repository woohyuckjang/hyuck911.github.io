print("-"*35)
print("   5주차 실습과제 : 2021136114-장우혁")
print("-"*35)
# 구구단 옆으로 찍기
'''
for i in range(2,10):
    print(i,"단")
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end="  ")
    print()

for i in range(1,10):
    print(i,"단")
    for j in range(2,10):
        print(i,"*",j,"=",i*j,end="  ")
    print()
'''
# 별찍기
i=0
while i<3:
    i+=1
    print("*"*i)
print("-"*5)

i=4
while i<0:
    print(" "*i)
print("*")

i=3
while i>0:
    print("*"*i)
    i-=1
print("-"*5)

