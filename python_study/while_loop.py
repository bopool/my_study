# while 반복문
""" 여러 줄짜리 문자열....
while 조건:
    반복할 코드
""" 
# 조건이 참(True)인 경우에 코드를 계속 반복 : 반복하다가 False가 나오면 아래로 내려감. 
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)
# na = 1
# while na >= 10:
#     print(na)
#     na += 1

# += 연산자 
## 대입 연산자의 일종
## 더하기 연산 후 할당 
### n += 1은 n = n+1이라는 의미 
# 모든 산술연산자 동일하게 사용 가능
# -= 
# *=
# /=
# **=
# //=
# %=

# 이것도 가능하다. 
# s1 = "안녕"
# s1 += "하세요"

# # while 반복문을 활용하여 
# # 10부터 1까지 순서대로 출력하세요. 

# cnt = 10
# while cnt > 0: # while cnt >= 1
#     print(cnt)
#     cnt -= 1 


# # 커피자판기를 만들자
# money = 10000
# price = 1000
# coffee = 5 
# while money >= price: # money - price >= 0
#     print("커피를 구매했습니다.")
#     money -= price
#     coffee -= 1
#     print("남은 커피 : ", coffee)
#     if coffee == 0:
#         break 

# # break 명령어. while for 반복문을 즉시 종료한다. 자주 사용함 중요. 보통 특정 조건(if문)과 함께 사용한다. 

# # while 반복문을 활용하여 
# # 1부터 10까지 홀수만 출력한다. 

# a = 1
# while a <= 10:
#     if a % 2 == 1:
#        print(a)
#     a += 1 # 이거 들여쓰면 무한반복에 빠짐

# # continue
# # 반복문의 제일 처음으로 돌아감 
# # break와 continue 는 계속 잘 사용되는 키워드들이다. 

# # 짝수 x % 2 == 0 
# # 홀수 x % 2 == 1
# #  
# # b = 0 
# # while b <= 10:
# #     if b % 2 == 0:
# #         continue # if문의 조건이 True면 continue 만나서 print를 못 만나고 while로 돌아간다!!!
# #     b += 1
# #     print(b)
# # 무한반복됨

# # ac = 0 
# # while ac < 10:
# #     if ac % 2 == 0:
# #         continue
# #     print(ac)
# #     ac += 1
# # 무한반복됨

# b = 0    
# while b <= 9:
#     b += 1
#     if b % 2 == 0:
#         continue # if문의 조건이 True면 continue 만나서 print를 못 만나고 while로 돌아간다!!! 
#     print(b)
# # 이것만 맞아요~

# 무한 반복문
# 무한 루프 
# 컴퓨터 프로그램은 대부분 무한 루프 위에서 실행되다가 종료 명령을 통해 종료된다고 보면 됨
# 조건식에 True를 입력해 항상 참이 되도록 하여 무한히 반복하게 한다. 
# while True:
#     user_input = input("종료하려면 1을 입력해 주세요.")
#     if user_input == "1":
#         break
# terminal 창에 커서 놓고 ctrl+C 하면 무한반복 종료됨. 


# 무한 반복문으로 계산기 만들기 
# +, -, *, / 계산 
# 2개의 수를 계산 a + b

# while True:
#     print("""
#     계산기
#     =======
#     1. 더하기(+)
#     2. 빼기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     """)
#     operator = input("계산을 선택하세요 : ")
#     if operator  == "1": # 파이썬은 데이터 타입을 맞춰줘야 한다.
#         print("1 + 2 =", 1 + 2)
#     if operator  == "2":
#         print("1 - 2 =", 1 - 2)
#     if operator  == "3":
#         print("1 * 2 =", 1 * 2)
#     if operator  == "4":
#         print("1 / 2 =", 1 / 2)

#         # 어떤 계산을 할지, 어떤 숫자를 넣을지 입력할 수 있도록 
#         # q를 입력하면 종료되도록 변경하세요. 

# while True:
#     print("""
#     계산기
#     =======
#     1. 더하기(+)
#     2. 빼기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     """)

#     num = 1

#     operator = input("계산을 선택하세요 : ")
#     a = int(input("숫자를 입력하세요."))
#     b = int(input("숫자를 입력하세요."))

#     if operator  == "1": 
#         print(a, "+", b, "=", a + b)
#     elif operator  == "2":
#         print(a, "-", b, "=", a - b)
#     elif operator  == "3":
#         print(a, "*", b, "=", a * b)
#     elif operator  == "4":
#         print(a, "/", b, "=", a / b)
#     elif operator == "q":
#         break


# #    여러 개의 if를 사용할 때는 elif로 묶어주는 게 좋다. 

# 사용자가 가지고 있는 돈을 입력받는다. 
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다. 
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다. 
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다. 
# 커피는 500원 음료수는 700원 콜라는 930원 
# 물품의 개수는 무한하다고 가정한다. 
# while 반복문을 사용하여 작성한다. 

# 반복문과 리스트를 어떻게 함께 사용할지 !! 
# 변수들에게 대응을 할 수 있도록 일반화해서 작업한다. 

# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈:"))
# while idx < len(prices) : # while idx < 3:
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1


# 함수 이름을 외우는 게 아니라 내가 어떤 동작을 설계할 것인지가 중요하다. 

# while 반복문을 사용해서 
# scores 리스트에 시험 점수 5개를 
# 정수형으로 입력받으세요. 

# scores = []
# aa = 0

# while aa < 5:
#     score = int(input("시험 점수 : "))
#     scores.append(score)
#     aa += 1
#     print(scores)



# bb = 1

# while bb <= 9:
#     qq = bb * 2
#     print(2,"*",bb,"=",qq)
#     bb += 1 

bb = 1

while bb < 10:
    print(2,"*",bb,"=",bb*2)
    bb += 1
