"""
eng 변수, kor 변수, math 변수를 만들고 
각 변수는 과목의 시험 점수이다. 

영어점수는 80점
국어점수는 60점
수학점수는 50점

3과목 점수의 평균을 내고 
평균 점수에 따라 성적을 출력한다. 

A : 91 ~ 100
B : 81 ~ 90
C : 71 ~ 80
D : 61 ~ 70
F : 60 이하 

"""

# eng = 80
# kor = 60
# math = 50

# if (eng + kor + math) // 3 >= 91 < 100:
#     print((eng + kor + math) // 3, "A")
# elif (eng + kor + math) // 3 >= 81 < 90:
#     print((eng + kor + math) // 3, "B")
# elif (eng + kor + math) // 3 >= 71 < 80:
#     print((eng + kor + math) // 3, "C")
# elif (eng + kor + math) // 3 >= 60 < 70:
#     print((eng + kor + math) // 3, "D")
# else:
#     print((eng + kor + math) // 3, "F")

eng = input("영어 점수: ")
eng = int(eng)
kor = int(input("국어 점수: "))
math = int(input("수학 점수: "))

avg = (eng + kor + math) / 3

if avg >= 91:
    print("A")
elif avg >= 81:
    print("B")
elif avg >= 71:
    print("C")
elif avg >= 61:
    print("D")
else:
    print("F")


# input() 함수
# 사용자로부터 정보를 입력받는 함수 
# user_input = input()
# print(user_input)

# 정수형 변환 함수 : 파이썬에서는 바꿔준다. 
# 정수형, integer형, int형
# int(값) 
