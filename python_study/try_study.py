# 예외 처리 
# 오류 발생을 잡아내서 처리하는 것

# li = [1, 2, 3, 4, 5]
# li[100]
# # IndexError: list index out of range

# 100 / 0
# ZeroDivisionError: division by zero

# f = open("없는파일", "r")
# FileNotFoundError: [Errno 2] No such file or directory: '없는파일'


# 에러 발생 시 프로그램 중단. 에러 메시지를 보여준다. 


# 예외 처리 구문
# try ~ except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생했을 때 수행할 코드 
# 오류가 발생하지 않으면 except 블록의 코드는 실행되지 않는다. 
# try: 
#     100 / 0
# except ZeroDivisionError as e: # 에러발생 안하면 실행 안됨 
#     print("에러 발생")
# print("에러 발생 후")


# try: 
#     100 / 0
# except Exception as e: # Exception 에러객체를 이용하여 에러발생 하면 에러 메시지를 출력해줌   
#     print(e)
# print("에러 발생 후")
# 에러를 예외처리하고 에러 발생 메시지 "division by zero\n 에러 발생 후" 출력됨 


# try: 
#     100 / 0
# except ZeroDivisionError as e:    
#     print(e)
# print("에러 발생 후")
# 에러 잡아내서 예외처리하고 내용 체크 "division by zero\n에러 발생 후" 출력됨 


# 에러남 
# try: 
#     [1, 2, 3, 4, 5][100]
# except ZeroDivisionError as e:    
#     print(e)
# print("에러 발생 후")
# 조건으로 걸어둔 ZeroDivisionError가 아니라서 IndexError가 뜨고 먹통이 되어서 "에러 발생 후"도 뜨지 않는다.  

# try: 
#     [1, 2, 3, 4, 5][100]
# except ZeroDivisionError as e: 
#     print(e, "0으로 나눌 수 없습니다.")
# except IndexError as e: 
#     print(e, "인덱싱할 수 없습니다.")
# print("에러 발생 후")
# # 여러 개를 나열하여 에러를 예외처리하고 에러 내용을 체크할 수 있다. 에러 종류 메시지 출력됨 




# finally 
# 예외 발생 여부와 상관없이 항상 수행해야하는 코드

# try: 
#     f = open("없는 파일", "r")
# except:
#     print("에러 발생")
# finally:
#     f.close() 


# else 
# 오류가 발생하지 않으면 실행되는 코드 
# try:
#     age = int(input("나이: "))
# except:
#     print("입력이 잘못 되었습니다.")
#     print("숫자를 입력해주세요.")
# else:
#     if age >= 20:
#         print("성인입니다.")
#     else:
#         print("미성년입니다.")


# 아직 개발하지 않은 곳에서 일부러 에러를 발생시킨다. 에러남. 
# class Bird:
#     def fly(self):
#         raise NotImplementedError # raise 뒤에는 에러 객체 NotImplementedError가 와야 한다. 
        
# my_bird = Bird()
# my_bird.fly()
###############################

# my_calculator 모듈의 MyCalculator 클래스를 상속받아 MaxLimitCalculator 클래스를 정의하세요. 
# add, sub, mul, div 메소드를 사용하여 더하기, 빼기, 곱하기, 나누기를 할 수 있다. 
# 0으로 나눴을 대 에러가 발생하지 않도록 처리한다. 
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고, 100 이하의 값을 입력하도록 안내 메시지를 출력한다. 
# 계산 결과가 100보다 크면 계산하지 않고, 100이하의 결과가 나오는 값을 입력하도록 안내 메시지를 출력한다. 

