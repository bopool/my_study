def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__": # __name__ 특별한 변수들에 __ 언더바 두개로 표시를 해 주었다. import 했을 때, import 코드를 적어서 불러오는 파일-프로그램 실행하는 자리가 메인(__main__)이 되고, 불러온 것은 모듈 이름이 된다. 
    print(add(1, 2))
    print(sub(1, 2))

