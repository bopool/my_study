# 모듈
# 함수, 변수, 클래스 모아놓은 파이썬 파일 
# 다른 파이썬 프로그램에서 불러와서 사용 
# 파이썬 모듈 : 모아놓은 파이썬 파일 
# import 명령어로 불러옴 

"""
import 모듈이름

"""

# import my_module # my_module이라는 .py나 module 불러옴 // 모듈 자체를 호출함 호출한 파일에 있는 코드가 실행되어서 불필요한 연산이 있을 수 있다.  
# my_module.add(1, 2)
# my_module.sub(1, 2)

# """
# from 모듈이름 import 모듈함수 
# from 모듈이름 import 모듈함수1, 모듈함수2 
# from 모듈이름 import * # 전체 다 가져오겠다. 
# """

# from my_module import add, sub # 모듈에서 특정 함수만 호출함
# add(1, 2)
# sub(1, 2)


# from my_module import * # 모듈 내용 전체를 가져옴 
# add(1, 2)
# sub(1, 2)


# import my_module 
from my_calculator import MyCalculator
# my_calculator = MyCalculator()
# my_calculator.div(10, 0)
# ctrl+클릭 # 찾아들어가세요. 

# 숫자를 0으로 나누면 division by zero error 뜸


# 함수의 오류 부분은 재정의(덮어쓰기) 해준다. 
class ZeroCalculator(MyCalculator):
    def div(self, n1, n2): 
        if n2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print(f"{n1} / {n2} = {n1/n2}")


zero_calculator = ZeroCalculator()
zero_calculator.div(10, 0)


# error가 나면 그 아래부터 실행이 안되어서 잘 잡아내야 한다. 

# 예외처리 