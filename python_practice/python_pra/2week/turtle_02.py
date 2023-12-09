print("-"*35)
print("터틀 그래픽 : 2021136114-woohyuck")
print("-"*35)

## 함수 선언 부분 ##

## 변수 선언 부분 ##

## 메인 코드 부분 ##
import turtle
myT = turtle.Turtle()

myT.shape("turtle")
## 사각형
for i in range(0,4):
    myT.pencolor('blue')
    myT.pensize(10)
    myT.forward(200)
    myT.right(90)
    
myT.penup()
myT.goto(-300,300)

## 삼각형
myT.pendown()
myT.pencolor('red')
myT.pensize(10)
myT.forward(200)
myT.right(120)
myT.forward(200)
myT.right(120)
myT.forward(200)


turtle.done()
