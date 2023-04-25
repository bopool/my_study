# io : input/output

# 파일 입출력 
# 파이썬에서 파일 생성(파일 출력), 수정

# open()
# 파이썬 내장 함수
# 파일을 열고, 파일 객체를 리턴한다. 
# open(파일 이름(경로), 파일 열기 모드)
# f = open("C:/Users/405/my_study/python_study/새파일.txt", 'w') # 파일 객체 open()함수에서 값을 f에 넣는다. 
# f.close() # 꼭 해줘야 한다. 열었으면 닫아야지...



# 파일의 경로
# 절대 경로 : C:/ D:/ 처럼 최상단 경로부터 나타낸 경로 
# 상대 경로 : 현재 작업 위치부터 나타낸 경로 


# 파일 열기 모드 
# r : read 읽기 모드, 파일을 읽기만 할 때 사용 : 기존 파일 있어야 함. 추가/수정 불가 
# w : write 쓰기 모드, 파일에 내용을 쓸 때 사용 : 새로 만들거나 내용을 입력하고 싶을 때 사용, 내용이 덮어쓰기 된다. 
# a : add 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용 : 막줄 뒤에 내용 추가


# f = open("python_study/새파일.txt", 'w', encoding="utf-8")
# for i in range(1, 11):
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()


# print(모니터 창 터미널에 출력), f.write(파일로써 출력한다): 방식, 방법, 위치가 다르다 
# 메모장 ansi 대부분 그렇다. 
# 유니코드로 지정해서 열어야 

# f = open("python_study/새파일.txt", 'a', encoding="utf-8")
# for i in range(11, 21):
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()

# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# f.close()

# readline() 함수
# 첫번째 줄부터 줄바꿈까지 한 줄씩 읽어온다. 
# 커서가 이동하는 것처럼 읽어옴 

# 전체 읽어오기
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# while True:
#     line = f.readline()
#     if line == "":
#         break
#     print(line)
# f.close()

# readlines() 함수
# 파일의 모든 줄을 읽어서 리스트[]로 반환 
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# print(lines)
# f.close()

# 한 줄 씩 읽도록 출력
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# read() 함수 
# 파일 내용 전체를 문자열 한 덩어리로 리턴한다. 
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# data = f.read()
# print(data)
# f.close()


# for문으로 읽기 : readline for문으로 전체 읽어온 것처럼 가져옴 
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f.close()

# with문 : a를 사용하는데 컨텍스트가 있는 객체에서 사용한다. 그런데 기존 파일이 없다면 새로 생성함. 
# open - close를 자동으로 해 준다. 탭 안쪽 내용 작동하는 동안만 열어두겠다. 
# f.close() 안 해줘도 되어서 조금 더 안전하게 사용 가능
# with open("python_study/새파일.txt", 'a', encoding="utf-8") as f:
#     f.write("end of file")

# 확장자가 없는 파일이 가능하다. 윈도우즈는 확장자가 있는 게 원칙. 

##################################################

# csv (comma separated values) 
# 어떤 곳에서도 사용할 수 있도록 ,와 엔터로만 구분된 값들을 모아놓은 파일 
# 데이터를 쉼표(또는 탭)와 엔터로 구분. 데이터들을 주로 많이 csv형태로 놓음 
# 이름,입실시간,퇴실시간
# 권오천,09:20,18:10
# 김예진,09:25,18:11
# 데이터 불러와서 처리한다. 
# with open("python_study/data.csv", "w", encoding="utf-8") as f:
#     f.write("날짜,날씨,기온\n")
#     f.write("20230424,맑음,10\n")
#     f.write("20230425,비,9\n")
# with open("python_study/data.csv", "r", encoding="utf-8") as f:
#     data = f.readlines
#     print(data)



# 계산 결과 저장 함수 
# 정수 2개를 입력받고 두 수를 더한 결과를 add_result.txt 파일에 저장하는 함수를 정의하세요. 
# 함수 이름 : add_write

# def add_write(a, b):
#     result = str(a + b)
#     with open("python_study/add_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)

# add_write(9, 6)


# def add_write(a, b):
#     result = a + b
#     with open("add_result.txt", "w", encoding="utf-8") as f:
#         f.write(str(result))

# add_write(1, 2)

# 텍스트 파일에 적힌 정수 2개를 읽어와서 더하는 함수를 정의하세요. 
# 텍스트 파일 이름은 : add_number.txt
# 경로 : python_study/add_numver.txt
# 정수 2개를 더한 결과를 print 하세요. 
# 함수 이름 : read_add_print


# with open("python_study/add_numver.txt", "w", encoding="utf-8") as f:
#     f.write("2,3")


def read_add_print():
    with open("python_study/add_numver.txt", "r", encoding="utf-8") as f:
        data = f.read()
        a = int(data[0])
        b = int(data[2])
        print(a + b)

read_add_print()

# 데이터 형태를 확인해야 데이터를 활용할 함수도 짤 수 있다..




