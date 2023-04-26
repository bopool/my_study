# 객체지향(oop, object oriented programming)
# python, JAVA, C++, C# 등 
# 객체와 객체 사이의 상호작용으로 프로그램을 구성하는 프로그래밍 패러다임 

# 객체지향의 특징
# 추상화 : 공통된 속성이나 기능 도출 member, method 주요 특징만 남기는 것
# 캡슐화 : 데이터의 구조와 연산을 결합시킨다. 
# 상속 : 상위 개념의 특징이 하위 개념에 전달된다. 
# 다형성 : 유사 객체의 사용성을 그대로 유지 다른 기능을 추가하거나 달라질 수 있다. 


# 객체는 추상화와 캡슐화의 결과 
# 객체는 데이터 필드와 메소드를 가진다. 

# 클래스(붕어빵틀)는 객체(붕어빵)를 정의한 것(객체의 설계도)
# 데이터 필드(멤버 변수, 속성) 
# 객체가 가지고 있는 변수 

# 메소드 
# 객체가 가지고 있는 함수


"""
class 클래스이름:
    클래스멤버변수 
    메소드
"""

# 클래스 이름도 변수 이름 규칙 지켜야 함
# 클래스 이름 컨벤션(관용: 에러는 안나지만 다들 지키고 있고 지켜야 편하고 좋음)
## 첫 글자 대문자
## 언더바(_) 안 쓰기
## 단어 구분될 때 대문자 

# class Car:
#     def move(self):
#         print("move")

# # Car라고 하는 클래스를 통해서만 호출할 수 있다. 
# # 클래스가 가지고 있는 함수, 클래스 안에 있는 함수를 메소드라고 한다. (메소드, 멤버스) 
# my_car = Car() # my_car 변수를 생성하여 객체가 된 "Car()"객체를 할당해 준다. 
# my_car.move()

# class SportsCar:
#     pass

# # 커멜 ..?



# # instance 인스턴스
# # 클래스를 통해 생성된 
# # 메모리 형태로 데이터에 저장되어 있겠죠. 
# # 인스턴스와 객체 같은 건데 
# # my_car는 Car() 클래스의 인스턴스 
# # my_car 인스턴스, Car()클래스, my_car변수 등 모두 my_car에 들어 있는 값을 말한다. 

# # . 객체 멤버 접근 연산자 
# # 리스트도 객체임. .을 통해 멤버에 접근하는 거.. 
# li = [1, 2, 3, 4, 5]
# li.append(6)

# # 파이썬에서는 모든 것이 객체다


# # 내장함수 type()
# print(type(li)) # <class 'list'>

# n = 10 
# print(type(n)) # <class 'int'>
# print(type("hello")) # <class 'str'>


# # str(문자열) 메소드

# # upper()
# # 모두 대문자로 변경
# s = "Hello"
# print(s.upper())

# # lower()
# # 모두 소문자로 변경
# s1 = "Hello"
# print(s1.lower())

# # strip()
# # 문자열 양쪽 끝의 특정 문자를 제거 
# s2 = "           Hello       "
# print(s2.strip())

# # lstrip(), rstrip()
# # 왼쪽 오른쪽 끝의 특정 문자 제거 
# print(s2.lstrip())
# print(s2.rstrip())

# # split() 
# # 구분자로 분할하여 리스트로 반환 
# # 잘 쓰임. 
# s3 = "Hello,World,Python"
# print(s3.split())

# # replace()
# # 처음에는 바꾸고 싶은 문자, 뒤에는 바꿔 넣고 싶은 문자 
# # 원본 수정한 게 아니라 새로운 문자열을 만들어 내는 것이다. immutable 리턴값을 출력한 거임. 
# print(s3.replace(',', ' ')) # Hello World Python 새로운 데이터를 만들어냈다. 
# print(s3) # Hello,World,Python 이렇게 원본은 그대로 있다. 

# # 재할당 --- 화살표 바꾼 거임 
# # 수정은 그 위치의 데이터를 변경한 거임 

# # string은 immutable 수정이 안된다. 

# s4 = "Hello"
# s5 = s4.lower() # s5 = s4.replace("H", "h") # 이렇게 해도 같다 얘들은 재할당이에여
# print(s5)



# self 매개변수(parameter)
# 모든 메소드의 첫번째 매개변수 
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음
# 객체 자신을 참조하여(class안에서) 클래스에 정의된 멤버에 접근할 때 사용. self = Person 

# class Person:
#     def say(self):
#         self.name = "사람1"
#         print("Hello")
#     def move(self):
#         pass
#     def eat(self, food):
#         print(f"{food}을 먹었습니다.")
#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다.")
# person1 = Person()
# person1.say()
# person1.eat("밥")
# person1.sleep()
# 객체를 만들고 변수에 넣어서 호출
# 호출은 변수.메소드() self라는 파라미터는 넣지 않아요

# initializer 
# 초기자 
# initialize 초기화 할 때 하는 일들을 정의하는 것
# instance를 initialize한다. 값을 가지게 한다. 
# instance가 생성될 때, 변수에 객체의 값을 할당할 때 생긴다. 
# class의 초기값 입력받을 때 사용됨 

# class Person:
#     def __init__(self, name, age, gender, phone): # initialize할 때 자동 호출되는 함수
#         self.name = name 
#         self.age = age 
#         self.gender = gender 
#         self.phone = phone 
#         print("initialize")
#     def say_name(self):
#         print(self.name)
# print("before")
# person2 = Person("이름", 20, "남자", "010-1234-5678")
# print("after")
# person2.say_name() # 멤버 변수를 사용할 때 self.를 사용하고. 다른 메소드에서는 초기화에 정의한 것을 사용하는 게 일반적이다.  





# Person 클래스에 introduce 메소드(클래스 안에 있는 함수)를 추가 
# 이름, 나이, 성별을 print하는 메소드 

# class Person:
#     def __init__(self, name, age, gender, phone): # initialize할 때 자동 호출되는 함수
#         self.name = name 
#         self.age = age 
#         self.gender = gender 
#         self.phone = phone 
#         print("initialize")
#     def say_name(self):
#         print(self.name)
#     def introduce(self):
#         print(f"안녕하세요. 저는 {self.name}입니다.") 
#         print(f"나이는 {self.age}살이고, 성별은 {self.gender}입니다.") 
#         print(self.name, self.age, self.gender)

# print("before")
# person2 = Person("김땡땡", 20, "남자", "010-1234-5678")
# print("after")
# person2.say_name() # 멤버 변수를 사용할 때 self.를 사용하고. 다른 메소드에서는 초기화에 정의한 것을 사용하는 게 일반적이다.  
# person2.introduce() # 안녕하세요. 저는 김땡땡입니다.\n나이는 20살이고, 성별은 남자입니다.\n김땡땡 20 남자 # 이렇게 출력됨 



# inheritance 상속 (유산)

# class Animal:
#     def __init__(self, name): # initialize 메소드 매개 변수 name 값 입력받음
#         self.name = name # 멤버 변수에 저장. 위 아래 name은 값이 같은 다른 변수!
#         print(f"{self.name}가 생성되었습니다.")
    
#     def say(self):
#         print("")

# class Dog(Animal): # 부모 클래스인 Animal class 객체를 상속받아서 Dog class 객체를 만들겠다.
#     # 상속받은 인스턴스의 메소드 재정의, 메소드 오버라이딩 method overriding(덮어쓰기)
#     def say(self):
#         print("멍멍") 

# my_dog = Dog("백구")
# my_dog.say()

# class Cat(Animal):
#     def say(self):
#         print("야옹")

# my_cat = Cat("달래")
# my_cat.say()


# 공통된 요소를 사용하여 데이터를 손쉽게 가공할 수 있다. 
# 관계형 데이터 베이스 (표의 형태로 저장되어 있음)
# 객체 관계형 데이터 베이스 : 한 줄씩 추상화해서 일반화하니까 객체화해서 사용할 수 있다. 같은 형식으로 만들고 같은 동작으로 움직이게 만들면 프로그래밍해서 사용하기 좋다.  
# 다른 많은 프로그래밍 언어에서도 관계형 데이터 베이스 사용함


# 나중에 데이터 베이스 할 때 여러가지 개념을 배움 protected private bector sector 
# 오후엔 모듈

class Student:
    def __init__(self, name, age, school, grade):
        # 이름, 나이, 학교, 학년을 멤버변수로 저장하는 메소드를 만드세요.. 
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
    
    def introduce(self):
        # 이름, 나이, 학교, 학년을 print하는 method를 정의하세요. 
        print(f"{self.name}, {self.age}, {self.school}, {self.grade}")

stu1 = Student("홍길동", 20, "서울대학교", 1)
stu2 = Student("손흥민", 21, "서울대학교", 2)
stu3 = Student("류현진", 22, "서울대학교", 3)

stu_list = [stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce()