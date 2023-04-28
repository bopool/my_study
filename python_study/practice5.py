# 거꾸로 배열해도 같은 단어 또는 문장이 되는
# 회문인지 판별하는 함수를 정의하세요. 
# 함수에 문자열을 입력받고 회문이면 True
# 아니면 False를 반환하도록 정의하세요. 
# 함수 이름 : is_palindrome
# 반환 값 : True 또는 False


# palindrome = input("문자를 입력하세요.")
# def is_isplindrome(input_string):
#     # input_string : 회문 
#     input_string = input_string.replace(" ", "") 
#     length = len(input_string)
#     for i in range(length//2): # 반만 검사하면 되고, 정수만 수에 넣으려고 // 씀. 이 예제의 포인트!
#         if input_string[i] != input_string[length - 1 - i]:
#             return False
#     return True

# result = is_isplindrome(palindrome)
# print(result)


# palindrome = input("문자를 입력하세요.")
# def is_isplindrome(input_string):
#     input_string = input_string.replace(" ", "") 
#     return input_string == input_string[::-1]

# result = is_isplindrome(palindrome)
# print(result)




# 내장 함수
# reversed("안녕하세요") # 원본은 그대로 두고 return이 뒤집힌 새로운 게 나온다. immutable한 것도 처리됨. 
# for i in () # 위에 글자 reversed 하려면 for문을 서서 strip을 해 주고, string3 = "".join(string2)  이런 것도 해 줘야 함. 

def get_biggest(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    numbers.sort(reverse=True)
    map(numbers, str)
    result = "".join(numbers)
    for i in numbers : 
        result += str(i)
    return int(result)
print(get_biggest("안", "녕", "하", "세", "요"))

# li1 = [1, 2, 3, 4, 5]
# li1.reverse() # 원본이 뒤집힙니다. 

# 리버스랑 스트립
# cpu 자원 아끼는

# string3 = "".join(string2)
# for line in f:
#         print(line.strip())

# https://www.acmicpc.net/ 공부해보자! 
# https://swexpertacademy.com/main/main.do 학습자료가 있다. 
# https://www.programmers.co.kr/ 문제 풀 때 테스트도 할 수 있다. 
# 꾸준히 문제를 풀면 좋을 것 같습니다!


# 시험문제

# def solution(my_string, n):
#     answer = ''
#     if 1 <= len(my_string) <= 1000 and 1 <= n <= len(my_string):
#         answer = my_string[:n]
#     return answer

# def solution(my_string, n):
#     return my_string[:n]


# 데이터 크롤링

