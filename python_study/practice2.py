# li_1 = ["Hello", "World", "Python"]
# # li_1의 원소를 사용하여 
# # Hello world Python 이라고 출력하세요. 


# print(li_1[0], li_1[1], li_1[2])

# # join(리스트)
# ## 리스트의 문자열을 합치는 함수
# print(" ".join(li_1))

# print(li_1[0] + " " + li_1[1] + " " + li_1[2])

# ####################################

# li_1 = ["Hello", "World", "Python"]

# # li_1의 원소를 사용하여 
# # HelP라고 출력하세요. 
# print(li_1[0][0:3] + li_1[2][0])
# print(li_1[0][0] + li_1[0][1] + li_1[0][2] + li_1[2][0])

# ####################################

# li_1 = ["Hello", "World", "Python"]
# li_2 = [1, 2, 3]
# # 1i_1과 li_2를 사용하여 
# # ["Hello", "World", "Python", 1, 2, 3]
# # 를 출력하세요. 
# print(li_1 + li_2)

# li_1.extend(li_2) # . 앞의 변수가 실행한다. 
# print(li_1) # 위의 + 연산자를 사용할 때와 달리, extend()는 1번 list를 변하게 한다. 

# ####################################

# # 1i_1과 li_2를 사용하여 
# # ["Hello", 1, "World", 2, "Python", 3]
# # 를 출력하세요. 


# li_1 = ["Hello", "World", "Python"]
# li_2 = [1, 2, 3]

# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.insert(5, li_2[2])
# # 늘어나는 index 값에 유의하세요

# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.insert(li_2[2])

# print(li_1)

# ####################################


# """
# eng 변수, kor 변수, math 변수를 만들고 
# 각 변수는 과목의 시험 점수이다. 

# 영어점수는 80점
# 국어점수는 60점
# 수학점수는 50점

# 3과목 점수의 평균을 내고 
# 평균 점수에 따라 성적을 출력한다. 

# A : 91 ~ 100
# B : 81 ~ 90
# C : 71 ~ 80
# D : 61 ~ 70
# F : 60 이하 

# """


# # 문제를 최대한 일반화해서 처리해야 한다. 
# # 하드코딩 직접 다 입력하면서 코딩하면 효율이 떨어진다.
# # 생략할 수 있는 건 생략하고, 합칠 수 있는 것을 합치는 것을 일반화한다고 한다. 

# scores = []
# scores = list() # 비어있는 리스트 생성 
# scores.append(int(input("영어 점수:"))) # 이렇게 함수를 여러개 호출할 수 있다. 안쪽부터 바깥 순으로 작동함
# scores.append(int(input("국어 점수:"))) 
# scores.append(int(input("수학 점수:"))) 

# avg = (scores[0] + scores[1] + scores[2]) / 3

# # sum() 합쳐주는 내장 함수
# # 리스트의 요소를 모두 더한다. 
# # 문자가 들어가 있으면 안됨!
# avg = sum(scores) / 3

# if avg >= 91:
#     print("A")
# elif avg >= 81:
#     print("B")
# elif avg >= 71:
#     print("C")
# elif avg >= 61:
#     print("D")
# else:
#     print("F")


# # input() 함수
# # 사용자로부터 정보를 입력받는 함수 
# # user_input = input()
# # print(user_input)

# # 정수형 변환 함수 : 파이썬에서는 바꿔준다. 
# # 정수형, integer형, int형
# # int(값) 

# ################################


# # 나이와 가지고 있는 돈을 입력받는다. 
# # 가지고 있는 돈으로 
# # 물건을 몇 개 살 수 있는지와 잔돈을 출력한다. 
# # 물건의 가격은 500원이다. 

# #나
# # pay1 = []
# # pay1 = list() # 비어있는 리스트 생성 
# # pay1.append(input("나이:"))
# # pay1.append(int(input("가지고 있는 돈:"))) 

# # avg1 = (pay1[1]) // 500 
# # avg2 = (pay1[1]) % 500 
# # print("살 수 있는 수량:", avg1, "/", "잔액", avg2)


# # #샘
# age = input("나이: ")
# money = int(input("돈: "))
# price = 500
# print(money // price)
# print(money % price)



# # ################################


# # 나이와 가지고 있는 돈을 입력받는다. 
# # 가지고 있는 돈으로 물건 별로 각각 
# # 몇 개 살 수 있는지와 잔돈을 출력한다. 
# # 물건의 가격은 1번 물건 1000원, 
# # 2번 물건 50원, 3번 물건 120원이다.  

# age = input("나이: ")
# money = int(input("돈: "))
# prices = [1000, 50, 120]
# print(money // prices[0], money % prices[0])
# print(money // prices[1], money % prices[1])
# print(money // prices[2], money % prices[2])

# # ################################