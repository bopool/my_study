weather = "맑음" # weatheer 변수에 값 할당
print("비가 오나요?", weather == "비") # weather의 값이 비와 같다는 비교연산식의 경우 결과가 프린트 된다. 비가 오나요? True 출력
if weather == "비": # weather 값이 "비"와 같으면 조건식이 True이므로 안쪽 코드 블록 실행 
    print("우산을 가져간다.")
elif weather == "맑음": #if로 들어가게 되면 elif에는 들어가지도 않음!
    print("날씨가 좋다.")
else:  # 조건식이 False이면 실행
    print("우산을 가져가지 않는다.")
# 끝. 프로그램 종료