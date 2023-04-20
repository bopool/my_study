"""
if 조건:
    실행하려는 코드
    코드2줄
    코드3줄
코드4줄
if문은 조건이 True(참)일 때만 안쪽 코드블럭을 실행

if 조건:
    조건이 참일 때 실행하려는 코드
else:
    아닐때 실행하려는 코드
else는 조건이 False(거짓)일 때 안쪽 코드 블럭을 실행

if 조건1:
    조건1이 True일 때 실행
elif 조건2:
    조건1은 False, 조건2는 True일 때 실행 
else: 
    조건1 False, 조건2 False일 때 실행
"""
# bool
# True(참), False(거짓)


number1 = 6 #숫자형 정수형 변수 
number2 = 6
if number1 > number2:
    print(number1 > number2)
    print("number1이 더 크다.")
elif number1 == number2:
    print(number1 == number2)
    print("number1과 number2가 같다.")    
else:
    print(number1 > number2)
    print("number2가 더 크다.")

# 비교 연산자 (a, b는 변수)
# a > b     a가 b보다 크다.
# a >= b    a가 b보다 크거나 같다. 
# a < b     a가 b보다 작다.
# a <= b    a가 b보다 작거나 같다. 
# a == b    a와 b가 같다. 
# a != b    a와 b가 같지 않다. 

print(2 > 3) # False
print(2 >= 3) # False
print(2 < 3) # True
print(2 <= 3) # True
print(2 == 3) # False
print(2 != 3) # True

print("a" < "b") # True 사전 순서대로 뒤로 갈수록 커짐
print("CAT" < "DOG") # True 첫글자 기준 
print("COW" > "CAT") # True 첫글자가 같으므로 두번째 글자 기준
print("DOG" == "dog") # False 문자열의 경우 로그인에 많이 쓰임!
print("DOG" > "dog") # False 대문자가 작음 

# 논리 연산자 (bool 연산자에 사용, True/False 피연산자에 적용)
# and   a and b     a와 b가 모두 True 일 때만 True, 아니라면 False
# or    a or b      a와 b 중 하나라도 True면 True, 둘다 False면 False
# not   not a       참True이면 거짓False으로 거짓False이면 참True으로 바꾸어 줌. 단항연산자

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True


age = 17
money = 10000

if age >= 20 and money >= 10000:
    print("성인이고 부자입니다.")
if age >= 20 or money >= 10000:
    print("성인 또는 부자입니다.")

# 문자나 숫자도 bool 형태로 적용된다. 0이 아니라면 1로 인식 문자가 들어있다면 1(True)이 되고 문자가 없다면 0(False)이 됨
if "안녕":
    print("안녕하세요")
# 숫자가 들어있는지 안 들어있는지 체크할 때 사용. 숫자는 0이면 False, 0이 아니면 True가 된다. 
if 0:
    print(0)


