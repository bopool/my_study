# 문자열 포매팅(formatting) 중요중요 자주 씀 
# result = str(a) + "+" + str(b) + "=" + str(a+b)
# 다양한 자료형을 문자열로 바꿀 수 있다. 위치, 다른 문자랑 자유롭게 사용할 수 있다. 

result = "%d + %d = %d" % (3, 2, 5)
print(result)

# a, b = 1, 2
# result1 = "%d + %d = %d" % (a, b, a+b) 
# print(result1)


# # 포맷 코드 
# # %s 문자열(string)
# # %d 정수(int)
# # %f 실수(float)
# # %o 8진수 
# # %x 16진수
# # %% % 글자 자체 

# string1 = "Hello"
# int1 = 3
# float1 = 1.2345

# print("%s %d %f" % (string1, int1, float1))



# # f-string 중요중요 자주 씀
# # Python 3.6 이후 버전부터 지원 
# # 직관적으로 사용하기 때문에 좋다. 
# string1 = "Hello"
# int1 = 3
# float1 = 1.2345
# result = f"string{string1} {int1} {float1}"
# print(result)



# # 계산기 문자열 포매팅으로 변경해 보기 
# def add(a, b):
#     result = "%d + %d = %d\n" % (a, b, a+b)
#     print(result)
#     with open("calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)

# def sub(a, b):
#     result = "%d - %d = %d\n" % (a, b, a-b)
#     print(result)
#     with open("calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)

# def mul(a, b):
#     result = "%d * %d = %d\n" % (a, b, a*b)
#     print(result)
#     with open("calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)

# def div(a, b):
#     result = "%d / %d = %d\n" % (a, b, a/b)
#     print(result)
#     with open("calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)

# while True:
#     print("""
#     계산기 표시
#     1: +
#     2: -
#     3: *
#     4: /
#     q: 종료
#     """)
#     operator = input("원하는 계산을 입력하세요.")
#     if operator == 'q':
#         break
#     a = int(input("정수 1: "))
#     b = int(input("정수 2: "))
#     if operator == "1":
#         add(a, b)
#     elif operator == "2":
#         sub(a, b)
#     elif operator == "3":
#         mul(a, b)
#     elif operator == "4":
#         div(a, b)


# 계산기 f-string 포매팅으로 변경해 보기 
def add(a, b):
    result = f"{a} + {b} = {a+b}\n"
    print(result)
    with open("calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(result)

def sub(a, b):
    result = f"{a} - {b} = {a-b}\n"
    print(result)
    with open("calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(result)

def mul(a, b):
    result = f"{a} * {b} = {a*b}\n"
    print(result)
    with open("calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(result)

def div(a, b):
    result = f"{a} / {b} = {a/b}\n"
    print(result)
    with open("calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(result)

while True:
    print("""
    계산기 표시
    1: +
    2: -
    3: *
    4: /
    q: 종료
    """)
    operator = input("원하는 계산을 입력하세요.")
    if operator == 'q':
        break
    a = int(input("정수 1: "))
    b = int(input("정수 2: "))
    if operator == "1":
        add(a, b)
    elif operator == "2":
        sub(a, b)
    elif operator == "3":
        mul(a, b)
    elif operator == "4":
        div(a, b)

