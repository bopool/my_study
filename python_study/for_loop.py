# for문
"""
for 변수 in iterable값:
    반복할 코드

iterable이터러블 뽑아내거나 슬라이싱 할 수 있는 데이터가 연결된, 반복 가능한 것들 : 문자열, 리스트 등 

"""


# 첫번째 요소부터 마지막 요소까지 
# 변수에 대입하면서 반복
# li_1 = ["one", "two", "three"]
# for i in li_1: 
#     print(i)

# s1 = "hello"
# for i in s1:
#     print(i)


# 무한반복은 while에서만 가능하다. for문은 무한반복 안 됨
# for는 꺼내서 반복하는 거라서..

# for문에서 사용하는 값들은 기본적으로 정수다. 


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)

# numbers.reverse()
# for number in numbers:
#     print(number)

# range()
# range(끝 정수)            # 0 ~ 끝 정수 - 1 레인지 객체가 만들어졌다
# for i in range(10): # 0 ~ 9 반복횟수는 10
#     print(i)

# range(시작, 끝)           # 시작 ~ 끝 - 1
# for i in range(1,11): 
#     print(i)

# range(시작, 끝, 스텝)     # 시작 ~ 끝 - 1 까지인데 스텝만큼 차이나게 
# for i in range(1, 21, 3): 
#     print(i)

# 레인지 파이썬 내장 함수 

# 데이터 값 :: 객체 object


# # for 문을 사용하여 2부터 30까지 출력해 보세요. 
# for i in range(2, 31):
#     print(i)

# # for 문을 사용하여 2부터 30까지 숫자 중 짝수만 출력해 보세요. 

# for i in range(2, 31, 2): # 짝수만 가져오기 때문에 전체 다 출력해도 된다. 
#     print(i)

# for i in range(2, 31):
#      if i % 2 == 1: # 홀수
#           continue # pass : 해당 구문 안에서는 아무것도 안하고 넘어갈 때. 반복문 조건문 등 미정일 때 활용하기 좋음 continue는 무조건 구문 처음으로 돌아감
#      else:
#          print(i) # 홀수 아닌 것 == 짝수 출력

# for i in range(2, 31):
#      if i % 2 == 0: # 짝수 
#          print(i)

# for 문을 사용하여 10부터 1까지 출력해보세요. 
# for i in range(10, 0, -1):
#     print(i)

# for i in reversed(range(1, 11)):
#     print(i)

# for i in range(1, 11)[::-1]:
#     print(i)
# # slicing 슬라이싱 [시작인덱스:끝인텍스:방향]


## 구현하는 방법은 여러가지다. 상황에 따라 적절함이 다를 수 있다...
# while문으로 쓴 건 for문으로 만들 수 있다. 


# for문 자판기를 만들어보자 
# money = 10000
# price = 1000
# coffee = 5 
# for i in range(5): # 0 ~ 4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 : ", coffee - 1 - i) # 4 ~ 0

# # 숫자 변수 흐름이 예측이 안되어서 그렇다. 

# for i in range(1, coffee + 1): # 1 ~ 5
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 : ", coffee - i)

# for i in range(coffee): 
#     print("커피를 구매했습니다.")
#     money -= price 
#     coffee -= 1
#     print("남은 커피 : ", coffee)


# 더 이상 사지 못할 때 구매 멈추기 
# money = 2000
# price = 1000
# coffee = 5 
# for i in range(5): # 0 ~ 4
#     print("커피를 구매했습니다.")
#     money -= price # money = money - price
#     print("남은 커피 : ", coffee - 1 - i) # 4 ~ 0
#     if money < price:
#         break


# 레인지 객체 만들어서 포문 돌리면 
# 횟수가 정해져 있는 반복 돌릴 때 좋다. 
# 횟수 파악할 때. 
# 그 외에도 포문에 여러 장점이 있음 

# while 특정 시점까지 뭔가가 달성될 때 까지 반복하는 데 효과적이다. 


# 음료수 가격 ::: 
# for문이 잘 사용되는 이유를 보여주는 예제
# prices = [500, 700, 930]
# money = int(input("돈:"))
# for i in range(len(prices)): # i를 index의 숫자로 쓸 수가 있다. 
#     price = prices[i]
#     print(money // price)
#     print(money % price)

# 가장 효율적인 for문 사용법
# prices = [500, 700, 930]
# money = int(input("돈:"))
# for price in prices: # prices에 있는 값들을 꺼내서 price에 힘시로 하나씩 넣어서 계산해서 보여줌. 
#     print(money // price)
#     print(money % price)


# 시험점수 5개 입력 
# scores = []
# for i in range(5):
#     score = int(input("시험점수:"))
#     scores.append(score)

# 구구단 2단
# for i in range(1, 10):
#     print("2 *", i, "=", 2*i)

# 이중 for문 : 안쪽의 작은 루프부터 시작한다. 
# 가로(탭) 세로(줄) 위치 모두 중요하다!!!!!!!!
for i in range(2, 10):
    print(i,"단")
    for j in range(1, 10):
        print(i,"*", j, "=", i*j)
    print("-------------")
    