# 계산기 만들기 
# 기능 : 두 정수의 사칙연산(+, -, *, /)
# add(), sub(), mul(), div() 함수 정의 
# input() 함수를 활용하여 정수 2개, 사칙연산 선택을 입력받은 후 계산 결과를 print한다. 
# 계산식과 결과를 calculator_result.txt 파일에 기록한다. 
# 사용자가 'q'를 입력하면 종료한다.



# 경제적으로 코드 짜기 많이 보고 많이 직접 짜봐야 함.. 
# def add(a, b):
#     add1 = a + b
#     print(a, "+", b, "=", add1)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(str(a) + "+" + str(b) + "=" + str(add1))

# def sub(a, b):
#     sub1 = a - b
#     print(a, "-", b, "=", sub1)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(str(a) + "-" + str(b) + "=" + str(sub1))

# def mul(a, b):
#     mul1 = a * b
#     print(a, "*", b, "=", mul1)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(str(a) + "*" + str(b) + "=" + str(mul1))

# def div():
#     div1 = a / b
#     print(a, "/", b, "=", div1)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(str(a) + "*" + str(b) + "=" + str(div1))


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







# def add(a, b):
#     result = str(a) + " + " + str(b) + " = " + str(a+b) + "\n"
#     print(result)
#     with open("calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)

# def sub(a, b):
#     result = str(a) + " - " + str(b) + " = " + str(a-b) + "\n"
#     print(result)
#     with open("calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)

# def mul(a, b):
#     result = str(a) + " * " + str(b) + " = " + str(a*b) + "\n"
#     print(result)
#     with open("calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)

# def div(a, b):
#     result = str(a) + " / " + str(b) + " = " + str(a/b) + "\n"
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








# MyCalculator 클래스로 만들어보세요. 
# add, sub, mul, div 메소드 


# class MyCalculator():
#     def __init__(self, n1, n2):
#         self.n1 = n1
#         self.n2 = n2
#     def add(self, n1, n2):
#         print(f"{n1} + {n2} = {n1+n2}")
#     def sub(self, n1, n2):
#         print(f"{n1} - {n2} = {n1-n2}")
#     def mul(self, n1, n2):
#         print(f"{n1} * {n2} = {n1*n2}")
#     def div(self, n1, n2):
#         print(f"{n1} / {n2} = {n1/n2}")

# my_calculator = MyCalculator()


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
#     n1 = int(input("정수 1: "))
#     n2 = int(input("정수 2: "))
#     if operator == 'q':
#         break
#     for i in range(1, 5):
#         if operator == i:
            





class MyCalculator:
    def __init__(self):
        pass
    def add(self, n1, n2):
        print(f"{n1} + {n2} = {n1+n2}")
    def sub(self, n1, n2):
        print(f"{n1} - {n2} = {n1-n2}")
    def mul(self, n1, n2):
        print(f"{n1} * {n2} = {n1*n2}")
    def div(self, n1, n2):
        print(f"{n1} / {n2} = {n1/n2}")

if __name__ == "__main__": # 실행 부분만 들여줘야 한다. 
    my_calculator = MyCalculator()

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
        n1 = int(input("정수 1: "))
        n2 = int(input("정수 2: "))
        if operator == "q":
            break
        if operator == "1":
            my_calculator.add(n1, n2)
        elif operator == "2":
            my_calculator.sub(n1, n2)
        elif operator == "3":
            my_calculator.mul(n1, n2)
        elif operator == "4":
            my_calculator.div(n1, n2)
        else:
            print("잘못 입력하였습니다.")
        


