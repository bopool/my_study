# 표준 라이브러리 
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치 
# 따로 설치하지 않고 import 명령어로 불러옴
#  
# 관련 기능 별로 모듈을 만들어 둔다. 효율성을 위해. / 모듈을 모아 놓은 것을 패키지라고 함. 패키지와 모듈을 모아 놓은 것을 라이브러리라고 함. 


# datetime library ************
# 날짜 관련 라이브러리 
# datetime의 date 객체 사용 

# import datetime
# day1 = datetime.date(2023,4,17)
# day_end = datetime.date(2023, 9, 18)
# diff = day_end - day1
# print(diff.days)


# 2018년 8월 6일 무슨 요일일까요?
# weekday() --> 0:월요일 1:화 2: 수 ~ 6:일요일
# import datetime
# day = datetime.date(2018, 8, 6)
# weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"] # list 사용
# print(day.weekday())
# print(weekdays[day.weekday()]) # indexing 사용

# datetime의 포맷팅 코드 
# 날짜랑 시간 표시하는 방법 : 값은 같지만 표현방법이 다르다. 
# 년/월/일 
# 월/일/년
# 일/월/년
# 2023년 4월 27일
# 2023-04-27
# 23년 4월 27일

# import datetime
# today = datetime.datetime.today() # today()는 현재 시스템 시간을 가져옴
# # strftime()
# print(today.strftime("%Y년 %m월 %d일"))
# # # %Y 년도 4자리 다 출력 
# # # %y 년도 2자리 
# # # %m 월
# # # %d 일
# # # %H 시간(24시간 짜리로 출력)
# # # %I 시간(12시간 기준 표기)
# # # %M 분 (소문자 m은 월이니 헷갈리면 안됨)
# # # %S 초
# # # %A 요일 

# print(today.strftime("%A"))


# # datetime과 호환되면서 사용되는 Time library
# # 시간 관련
# import time
# time_now = time.time() 
# print(time_now) # 1970년 1월 1일 0시 0분 0초부터 지금까지의 초 1682560880.911193 출력됨
# print(time.strftime("%H:%M:%S", time.localtime(time_now))) # 지금 시간 11:06:15 출력됨



# UTC 세계표준시각 기준으로 재고 / 1970년 1월 1일 0시 0분 0초부터의 수가 나온다. 기준점 
# 랜덤값을 낼 때 계속 변하는 시간의 수를 활용하기도 함.  
# 어떤 기능이 있는지, 어떤 기능을 하는지 알아보려면 공식 사이트에서 확인하는 것이 좋다. 

# time.sleep()
# import time
# print("before")
# times= time.sleep(1)
# print("after")

# for i in range(10):
#     print(i)
#     time.sleep(1.2)

# 약 1초 쉬는 것임. 정확하게 계산하지는 않는다. 정확한 시간계산이 필요하면 파이썬보다는 기계어에 더 가까운 언어를 쓰는 것이 좋다. 
# 크롤링할 때 네이버 주식정보, 네이버 뉴스정보 긁어오기. 등등 로딩을 적당히 기다려줄 때 사용할 수 있다. 

# 몇분전, 계산


## math
## 수학 관련 
## 필요한 수학계산을 찾아서 쓸 수 있다. 
# import math
# result = math.ceil(1.1)
# print(result) # 올림이라 2 나옴 

# result = math.floor(1.9)
# print(result) # 내림이라 1 나옴 

# print(math.pi) # 3.141592653589793 파이값 나옴 


# random 
# 난수 관련 
# import random
# # random.random()
# # 0.0 ~ 1.0 사이의 실수 중 난수 값
# random_value = random.random()
# print(random_value)

# # random.randint(시작, 끝)
# # 시작~끝 사이의 정수 중 난수값 
# random_value = random.randint(1, 10) # for문의 range와 달리 1도 10도 포함된다. 
# print(random_value)

# # choice
# # random.choice(리스트) 
# # 리스트의 요소 중 무작위로 하나를 리턴 
# foods = ["서브웨이", "맥도날드", "짜장면", "국밥", "김치찌개"]
# food = random.choice(foods)
# print(food)

# # shuffle() 게임 만들기 
# li = [1, 2, 3, 4, 5]
# random.shuffle(li)
# print(li)

# lotto_numbers = list(range(1, 46))
# my_lotto = []
# for i in range(6):
#     random_value = random.choice(lotto_numbers)
#     if random_value not in my_lotto:
#         my_lotto.append(random_value)
#     # 호합 연산자 in/ not in 뒤에 시퀀스형 데이터가 온다.     
# print(my_lotto)

# 구현하는 방법은 여러가지 

# in 연산자 
# a in b
# a가 b에 포함되어 있으면 True
# a가 b에 포함되어 있지 않으면 False

# not in 연산자 
# a not in b
# a가 b에 포함되어 있지 않으면 True
# a가 b에 포함되어 있으면 False


# lotto_numbers = list(range(1, 46))
# random.shuffle(lotto_numbers)
# my_lotto = lotto_numbers[:6]
# print(my_lotto)


# 게임 만들 때 랜덤은 필수죠


# 색 이름과 음식 이름을 합치면 멋진 밴드 이름이 된다고 합니다. 색 이름과 음식 이름을 무작위로 뽑아 밴드이름을 추천하는 프로그램을 만들어 보세요. 
"""
베이지 블랙 블루 회색 청색 레드 파란 핑크 
주꾸미 요거트 오란다 와플 아이스티 떡볶이 커피 
"""

# colors = ["베이지", "블랙", "블루", "회색", "청색", "레드", "파란", "핑크", "차콜", "그레이"]
# animals = ["주꾸미", "요거트", "오란다", "와플", "아이스티", "떡볶이", "커피", "커피"]
# import random
# a = random.choice(colors)
# b = random.choice(animals)
# print(f"{a}{b}")


# 숫자야구게임
# 1. 정답을 정한다. 정답은 4자리 숫자(랜덤)
# 2. 게임 유저가 정답을 입력한다. 
# 3. 정답과 비교해서 S / B / O 개수 알려준다. 
# 4. 정답을 맞추거나, 종료를 입력하면 끝낸다. 
# 5. 정답을 맞췄을 때 "한번 더 하시겠습니까?" 


# 내가 뭐 할지 생각하면서 프로그래밍해야겠죠
# 코드는 위에서 아래로 순서대로 작동한다. 중간에 막혀서 넘어가지 못하면 동작 종료됨
# 개발 시 테스트를 반드시 하게 되는데, 어떤 문제가 생길 지 미리 생각해보는 연습을 해보는 것이 좋다. 
# 함수화 할 수 있는 것, 기능 단위별로 묶을 수 있는 능력을 키우는 것이 좋다. 


# import random
# numbers = list(range(10))
# random.shuffle(numbers)
# answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]

# while True:
#     user_input = input("정답은? ")
#     if user_input == "종료":
#         print("종료합니다.")
#         break
#     # 숫자로만 이루어진 문자열인지 확인한다. 숫자로만 이루어져 있으면 True 아니면 False
#     # 1. 만약 숫자가 아닌 값이 입력되면 다시 입력하게 한다. -->  2. 처음으로 간다 --> 3. continue 
#     if not user_input.isdigit():
#         print("숫자만 입력해주세요.")
#         continue
#     # 만약 4자리 숫자가 아니면 다시 입력하게 한다. 
#     # continue --- 처음으로 간다. 
#     elif len(user_input) != 4:
#         print("4자리 숫자만 입력하세요.")
#         continue
#     # 공백이 입력되면 어떻게 처리할까요
#     # 문자 " "이 있으면 사라지게 하기 strip() 등
    
#     # 첫 글자가 0인 경우  
#     elif user_input[0] == "0":
#         print("첫번째 숫자를 0이 아닌 다른 숫자로 바꿔주세요.")
#         continue
#     duplicate = False # 불린형 변수 만들고, 
#     for i in range(3):
#         if user_input[i] in user_input[i+1:]:
#             duplicate = True
#             break # 포문에서 벗어나서 while로 돌아가야 해서.. 
#     if duplicate:
#         print("중복된 숫자가 없게 입력하세요.")
#         continue
#     strike = 0
#     ball = 0
#     out = 0
#     for i in range(4):
#         input_value = int(user_input[i]) # 0, 1, 2, 3번째 글자가 i에 들어간다. for문 네번 돌아가면서 순차적으로 
#         if input_value not in answer:
#             out += 1
#         elif input_value == answer[i]:
#             strike += 1
#         else:
#             ball += 1

#     print(f"strike: {strike}, ball: {ball}, out: {out}")

#     if strike == 4:
#         print("정답!")
#         user_input == input("한번 더 하시겠습니까? [y/n]")
#         if user_input == "y":
#             numbers = list(range(10))
#             random.shuffle(numbers)
#             answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
#         else:
#             break

# 안녕하세요. 넣으면 안되게 에러 잡기 

            
# 문자라서 반복문 사용 가능 위에서 일부러 int 안함
    

# 삼항 연산자
# 참일때값 if 조건 else 거짓일때값
# 할당할 때 써준다. 조건이 참일 때 앞에 값, 거짓일 때 뒤에 값 적용됨 
# 복잡해보여서 안 좋아하는 사람도 있음. 적절하게 사용하세요. 

# result = "참" if True else "거짓"
# result = "참" if False else "거짓"
# print(result)

# ex)
# def is_odd_number(n):
#     return "홀수" if n % 2 == 1 else "짝수"



#     except Exception as e:
#         print("잘못 입력하셨습니다.")
#         break



# os 
# OS자원을 제어 (windows, 맥, linux)

# import os

# os.environ 시스템의 환경변수값을 리턴한다. 
# print(os.environ)
# 출력됨: environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\405\\AppData\\Roaming', 'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\LOCAL\\crashpad_9968_MYUKGABRDOVWNBOK', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-3NAELD1', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\405', 'LOCALAPPDATA': 'C:\\Users\\405\\AppData\\Local', 'LOGONSERVER': '\\\\WIN-15VQGN85T0N', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\405\\OneDrive', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT', 'PATH': 'C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Users\\405\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\405\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\405\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Users\\405\\AppData\\Local\\Programs\\Microsoft VS Code\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3c03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\405\\Documents\\WindowsPowerShell\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\405\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\405\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-3NAELD1', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-3NAELD1', 'USERNAME': '405', 'USERPROFILE': 'C:\\Users\\405', 'WINDIR': 'C:\\Windows', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.77.3', 'LANG': 'en_US.UTF-8', 'COLORTERM': 'truecolor', 'GIT_ASKPASS': 'c:\\Users\\405\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh', 'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\405\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Users\\405\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js', 'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-8217eaaaf7-sock', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONUNBUFFERED': '1'})

# # os.getcwd()
# print(os.getcwd())
# # 현재 경로를 절대경로 값으로 리턴한다. C:\Users\405\my_study
# # 상대경로를 주로 사용하기 때문에 절대경로값 확인이 매우 중요함.. 

# # os.mkdir(디렉터리)
# # 디렉토리를 만든다.
# os.mkdir("폴더1")
# 폴더1이 파이썬 프로그램 돌아가는 폴더 안에 만들어진다. 

# os.rename("원래이름", "바꿀이름")

# os.rmdir(디렉터리)
# 디렉터리를 지운다. 
# 폴더 안에 아무것도 없어야 함(비어있는 폴더여야 함)
# os.rmdir("빈폴더명")

# os.unlink("파일이름")
# 파일을 지운다.
# os.unlink("바꿀이름")
# 바꿀이름 파일이 사라졌다. 


# os.path
# 경로 경로를 따라가면서 관리한다..
# os.path.exists("경로")
# 파일이 있으면 True, 없으면 False

# import os

# if os.path.exists("없는파일"):
#     f = ("없는파일", "r")
# else:
#     print("파일이 없습니다.")


# if not os.path.exists("없는파일"):
#     f = ("없는파일", "w")
#     f.close()
# f = ("없는파일", "r")



# os.path.join("경로", "경로", "경로")
# 경로를 합쳐서 1개의 경로로 만들어준다. 
# 경로를 변수로 저장하는 경우가 많다. 
# import os
# cwd = os.getcwd()
# my_folder = "python_study"
# file_name = "test_file.txt"
# file_path = os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("테스트 파일을 작성합니다.")


# 외부 라이브러리 
# 파이썬 표준 라이브러리가 아닌 라이브러리 
# pip를 사용해서 설치한다. 

# pip
# package installer for python
# 파이썬 모듈, 패키지 설치하는 도구 
# numpy, pandas, matplotlib, scikit-learn, keras, Tensorflow, opencv, django...
# PyPI (Python Package Index) 파이썬 소프트웨어 저장 공간 / opensouce
# PyPI에 있는 파이썬 패키지를 설치해준다. 

# 패키지 설치(최신 버전 설치)
# pip install 패키지이름

# 패키지 삭제
# pip uninstall 패키지이름

# 특정 버전으로 설치 
# pip install 패키지이름==1.0.5 

# 최신 버전으로 업그레이드 
# pip install --upgrade 패키지이름

# 설치된 패키지 리스트 확인
# pip list

# 부등호로 몇 버전 이상/이하로 설정할 수도 있다. 관리할 수 있다. ..

# 패키지 배포 
# 의존성... 이미 있는 패키지 위에 .. 22 쓰기 위해서 써야 할 22 명시해야 함. .