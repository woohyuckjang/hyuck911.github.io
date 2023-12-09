# for문 (반복문)
# 사용법
'''
for 변수명 in range(시작값, 마지막값+1, 증가식)
    반복문장

print("-"*35)
print("   for 반복 : 2021136114-장우혁")
print("-"*35)

#range(반복횟수)
for i in range(10):
    print(i,": Hello")
'''
# 줄바꿈 없이 출력 end=""

# 1 ~ 10
'''
for i in range(1, 11):
    print(i, "Hello")
'''
# 1 ~ 10까지의 수 중 짝수만 출력
'''
for i in range(2, 11, 2):
    print(i)
'''

# 1 ~ 10까지 출력하기
'''
for i in range(1, 11):
    print(i, end=" ")
'''
# 10 ~ 1까지 출력하기
for i in range(10, 0, -1):
    print(i, end=" ")
