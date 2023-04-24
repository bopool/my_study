# function 함수 
# 입력 -> 처리 -> 출력 
# input(입력)을 받아서 특정 작업(처리)을 수행하고 output(출력)을 반환한다. 
# 기능을 구현하기 위해 만들어 둔 코드의 묶음

# 내장 함수 Intrinsic function (built-in function)
# 파이썬이 기본적으로 제공해주는 함수들. 호출만 하면 기능을 사용할 수 있다. 
# print()
# len()
# zip()
# int()
# float()
# str()
# list()
# range()

#################################################

# # abs(값)
# # absolute의 약자 
# # 입력한 숫자형 데이터의 절대값을 반환한다. 

# # 절대값 출력됨 
# print(abs(100)) # 100
# print(abs(-100)) # 100
# print(abs(3.15)) # 3.15
# print(abs(-3.15)) # 3.15

# #################################################

# # sum(리스트)
# # 리스트 안의 숫자를 더한 값을 반환한다. 
# print(sum([1, 2, 3, 4, 5])) # 1+2+3+4+5 = 15출력됨

# #################################################

# # max(리스트)
# # 리스트 안에서 최대값을 찾아 반환한다. 
# print(max([10, 2, 3, 4, 5])) # 10출력됨

# #################################################

# # min(리스트)
# # 리스트 안에서 최소값을 찾아 반환한다. 
# print(min([10, 2, 3, 4, 5]))

# #################################################

# # 두 개 형식의 차이를 이해해야 한다. 

# # li_1 = [1, 2, 3]
# # min(li_1)

# # li_2.append(0)

# # 리스트의 함수 
# # 내장함수인데 리스트를 입력하여 사용한다. 

# #################################################

# # 아스키코드 유니코드(문자 표시 규칙) 
# # 문자를 숫자로 변환해서 계산해야 할 때가 있다. 

# # chr() 
# # 정수 1개를 입력받고 해당하는 유니코드 문자를 반환한다.
# print(chr(65)) # A출력됨

# #################################################

# # ord()
# # 문자 1개를 입력받고 해당하는 정수를 반환한다. 
# print(ord('A')) # 65출력됨

# #################################################

# # round(값) == round(값, 소수 자릿수가 0인 값)
# # round(값, 소수 자릿수) # 파라미터의 기본값
# # 반올림 함수
# # 정확도는 떨어지지만 필요할 때가 있다. 
# # 사용자한테 보여줄 때 너무 긴 수에 사용해도 좋다. 
# print(round(1.234)) # 1출력됨
# print(round(1.234, 2)) #1.23출력됨
# print(round(1.36, 1)) #1.4출력됨

#################################################


# 함수 정의 (define function)
# 함수 이름 name
# 함수 입력값 parameter
# 함수 결과값 return value

"""
def 함수이름(함수입력값):
    함수기능코드
    return 함수결과값
"""

# def 함수를 정의하는 명령어
# 함수 이름도 변수 이름처럼 규칙을 지켜서 지어야 한다. 
# 영어, 숫자, _만 사용
# 숫자로 시작하면 안됨
# 띄어쓰기하면 안됨
# 파이썬에서 이미 정해진 키워드 사용하면 안됨
# 내장함수 기존에 이미 정의된 함수 이름도 피하는 것이 좋음
# 파이썬은 내장함수와 내가 정의한 함수 이름이 같을 때 내가 정의한 함수를 부른다. 
# 직관적으로 짓는 것이 좋다. print_list 같이 기능을 추측하기 쉽도록. 


# def print_names(): # print_name은 입력값 없는 함수라고 함수를 정의함, return이 없는 함수
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")

# print_names() # print_names함수를 호출하여 이름들 한줄씩 출력됨


# def get_name():
#     return "유리아" # return값("유리아")이 있어서 get_name함수가 유리아를 반환하여 출력된다. 

# def print_my_name():
#     print(get_name())

# print_my_name()

# 'return이 있는 함수'가 있고 'return이 없는 함수(None이 있는 함수)'를 만들 수는 있는데. 
# 함수에 return 값이 있어야 다른 함수에서 불러서 사용할 수 있다. 

# a = print_names() 
# b = get_name() 

# print(a) # None 출력됨
# print(b) # 유리아 출력됨

####################################################################

# parameter
# 함수에 입력하는 값. 괄호 안에 입력하는 값. 
# 매개변수, argument 혼용

# def add(a, b): # 매개변수 괄호 안에 매개 변수를 입력해 줘라! 라고 정의함 // a, b는 parameter
#     return a + b

# def print_add(a, b): 
#     print(a + b)

# result = add(1, 2) # return 있는 함수라서 값이 3 나옴 // 여기서 1, 2는 argument
# print(result)

# 순서에 유의할 것. 먼저 print_add 함수 정의된 곳으로 가서 실행(print함) 그 다음 result변수로 할당되고 return값이 없는 함수이므로 None이 나온다. 
# result = print_add(1, 2) 
# print(result) # None

# return값이 없는 함수는 그냥 이렇게 간단하게 호출하면서 사용합니당 
# 그냥 함수 실행하면 끝임 나오는 값으로 다음 계산을 한다든지 하는 일을 할 수가 없음  

# 순서대로 자리 위치에 대응하여 parameter값을 전달받음 
# print_add("안녕", 1) # can only concatenate str (not "int") to str
# print_add(1, 2) # 3
# print_add("안녕", "하세요") # 안녕하세요
# print_add("하세요", "안녕") # 하세요안녕
# print_add(b="하세요", a="안녕") # 안녕하세요

###################################################

# 변수의 사용 범위가 달라서 그렇다 : 전역변수, 지역변수 
# 함수 안의 a, b 변수와 바깥의 a, b 변수는 다르다. 이름이 똑같아도 다른 변수다. 구분 잘 해야 됨. 다른 언어에도 다 있음. 차이를 잘 알아 두어야 합니다. 굉장히 중요합니다. 꼭 보셔야 합니다. 
# 함수 바깥 전역 변수 gloval 
# 함수 안에서만 사용되는 지역 변수 local # return으로 반드시 내보내 줘야 사용할 수 있다.   

# def swap_number(a, b):
#     temp = a
#     a = b
#     b = temp
#     print(a, b) # 스왑된 숫자를 
#     return a, b
# a = 1
# b = 2
# print("함수 호출 전", a, b)
# a, b = swap_number(a, b)
# print("함수 호출 후", a, b)


###########################################


# 다음 함수를 정의하세요. 
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱

# n = int(input("숫자1: "))
# m = int(input("숫자2: "))

# def mul(n, m):
#    return n * m

# result = mul(n, m)
# print("답: ", result)

# 점유율이 높을 수록 좋은 자료 많고 가져다 쓸 수 있고 개발시간 단축시킬 수 있다. 

# debug 
# 다른 사람 코드를 가져와서 쓰려고 할 때 에러가 많이 난다. 
# 어디서 에러가 났는지 함수의 정의 부분까지 찾아가서 살펴봐야 함. 

"""

a = 1
b = 2
c = 3

각 변수에 숫자 하나씩 할당한 상황 
파이썬에서는 이런 표기가 가능하다

a, b, c = 1, 2, 3 # tuple 
d, e, f = [4, 5, 6] # list
g, h, i = (7, 8, 9) # tuple

a, b = 1, 2
a, b = 

"""

# default value parameter 기본값 매개변수. 자주 쓰인다, 매우 중요합니다. 
# 아래와 같이 값을 지정해서 정의할 수 있다. 
# 함수 호출 시 n2에 입력된 값이 없으면 기본값 사용
# def mul2(n1, n2=1):
#     return n1 * n2

# print(mul2(1, 2))
# print(mul2(1))


# def test_func(x, test=[]): # 비어있는 리스트를 매개변수에 할당. 절대 리스트를 기본값으로 사용하지 말 것 
#     test.append(x)
#     print(x, test)


# test_func(1) # [1]
# test_func(2) # [1, 2] list는 mutable 지역변수인데도 전역변수로 호출됨. 그래서 값이 누적된다. 


# def test_func(x, test=5): # 기본값이 immutable이라 변하지 않는다. 
#     test = test
#     print(x, test)


# test_func(1) # 5
# test_func(2) # 5 # 기본값이 immutable이라 변하지 않는다.


# def test_func(x, test=None): # 기본값이 immutable이라 변하지 않는다. 
#     if test == None: 
#         test = []
#     test.append(x)
#     print(x, test)


# test_func(1) # [1]
# test_func(2) # [2] # 기본값이 None일 때 리스트로 만들어 준다.


#####################################################


# 기본값이 있는 매개변수는 기본값이 없는 매개변수보다 뒤에 위치해야 함
# def sub(n1, n2=0, n3): # non-default argument follows default argument
#     print(n1 - n2 - n3)

# def sub(n1, n3, n2=0): # 이래야 에러가 안 남
#     print(n1 - n2 - n3)

# sub(10, 3) # sub함수 호출 7 출력



####################

# 1 ~ 10까지 더한다
# *를 사용한 매개변수
# 입력값이 몇 개가 될 지 모를 때(안 정해졌을 때 사용한다.)
# def add_many(*args): # args 바꿀 수는 있지만 관용적으로 사용되는 이름임
#     # 튜플처럼 사용
#     # 인덱싱, 슬라이싱
#     for i in args:
#          result += i
#     return result

# result1 = add_many(1, 2, 3, 4, 5)
# result2 = add_many(3, 2, 9, 4, 5)
# result3 = add_many(1, 2)

# print(result1)
# print(result2)
# print(result3)

###########################################

# def calc_many(n1, *args): # 순서 바꿔도 됨
#     result = n1
#     for i in args:
#         result += 1
#     return result

# a = calc_many(5, 3, 23, 4, 5)
# print(a)


# 키워드 매개변수 
# **kwargs
# keyword arguments 
# 딕셔너리로 사용할 수 있게 변수를 받아온다
# 유동적인 데이터를 입력할 때 사용
# def print_kewargs(**kwargs):
#     print(kwargs)

# print_kewargs(a=1, b=2) # {'a': 1, 'b': 2}
# print_kewargs(name='이름', age=10)  # {'name': '이름', 'age': 10}

# 파이썬 자체가 다이나믹한 언어여서 잘 모르고 갖다 쓸 때 에러가 발생할 확률이 높다.
# 함수 정의나 변수에 대한 설명이 있는 경우가 있고 없는 경우가 있다. 



##############################################


# # 함수의 반환 
# # return 반환값  
# # return을 만나면 반환값을 반환함과 동시에 종료된다. 
# def test_func5():
#     print(1)
#     print(2)
#     return None # None 값을 반환함과 동시에 함수 벗어남 
#     print(3)
#     print(4)
#     print(5)

# # 함수의 반환값은 무조건 1개이다. 매우 중요. 
# # def test_func6(a, b):
# #     return a + b
# #    return a * b # 위에서 끝나서 출력 안됨

# def test_func6(a, b):
#     return a + b, a * b # 여러 개의 값을 튜플 1개에 담아서 리턴해라 
# result = test_func6(1, 2)

# res_add, res_mul = test_func6(1, 2) 
# # res_add, res_mul = (a+b, a*b) # 위 줄과 같은 뜻이다. 

# print(result)









####################################################


# # *args, **kwargs 사용법 검색
# def func0(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for arg1 in kwargs.items():
#         print(arg1)    

# func0(10, 20, 'a',x=130, y=80, z='b')




# 쓰다 보면 받아들여진다... 
# 많이 찾아보고 써보면서 감을 잡는 것이 중요함. 반복숙달. 
# 백문이불여일타 : 안 보고 쳐보기 해야 실력이 는다

# 다음주: 데이터분석 데이터처리
# 머신러닝
