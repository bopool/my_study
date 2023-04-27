# 다음 함수를 정의하세요. 
# 정수 n을 입력받고, n보다 작은 수 중 3의 배수와 5의 배수를 모두 더한 합을 반환하는 함수

# 함수 이름 : sum_3_5


def sum_3_5(n):
    for i in range(n):
        if i % 3 == 0:
            i += 1
    for j in range(n):
        if j % 5 == 0:
            j += 1
    return i + j

nonot = sum_3_5(12)
print(nonot)

# def sum_3_5(n):
#     for i in range(n):
#         if i % 3 == 0 or i % 5 == 0:
#             result = i
#             i += 1
#     return result

# nonot = sum_3_5(12)
# print(nonot)

# or을 써보자 

# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0:
#             result += i
#         elif i % 5 == 0:
#             result += i
#         i += 1
#     return result

# printsum = sum_3_5(12)
# print(printsum)


# 정육면체 주사위 2개가 있다. 
# 2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조합을 모두 print 하는 함수를 정의하세요. 
# 함수 이름 : double_dice
# 출력 예시 
# 1, 2
# 6, 3

# def draw_dice():
#     for i in range(1, 7):
#         dice1 = i
#         for j in range(1, 7):
#             dice2 = j
#         print(dice1, dice2)

# draw_dice()

# def double_dice():
#     for i in range(1, 7):
#         for j in range(1, 7):
#             print(i, j)

# double_dice()

# def double_dice():
#     while i < 7:
#         i = 1
#         while j < 7:
#             print(i, j)
#             j += 1
#         i += 1

# double_dice()

# 이중 for문을 떠올리고, 파라미터 없고, 리턴 없다는 걸 떠올려라 

# dice = [1,2,3,4,5,6] 이용한 분도 있었음!



# 두 수의 차이를 구하는 함수 
# 함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하세요. 
# 함수 이름 : get_diff

# def get_diff(num1, num2):
#     ans1 = 0
#     if num1 > num2:
#         ans1 = num1 - num2
#     else num1 <= num2:
#         ans1 = num2 - num1
#     return ans1

# ans2 = get_diff(33, 81)
# print(ans2)

# def get_diff(a, b):
#     result = abs(a - b) 
#     return result





# 가장 큰 수를 만드는 함수 
# 함수에 입력된 5개 정수(0~9)를 정렬하여 만들 수 있는 가장 큰 수를 반환하는 함수를 정의하세요. 
# 함수 이름 : get_biggest


# def get_biggest(a, b, c, d, e): 
#     result = [a, b, c, d, e]
#     result.sort(reverse = True)
#     return result 

# resultin = get_biggest(1, 5, 2, 1, 1)
# print(resultin)


# def get_biggest(a, b, c, d, e):
#     numbers = [a, b, c, d, e]
#     numbers.sort()
#     result = 0
#     for i in range(len(numbers)):
#         result += numbers[i] * (10 ** i)
#     return result

# aa = get_biggest(2, 4, 5, 7, 8)
# print


# def get_biggest(a, b, c, d, e):
#     numbers = [a, b, c, d, e]
#     numbers.sort(reverse=True)
#     result = ""
#     for i in numbers : 
#         result += str(i)
#     return int(result)
# 파이썬의 문자/숫자를 다르게 왔다갔다 할 수 있는 특성을 사용한 코드

# def get_biggest(a, b, c, d, e):
#     numbers = [a, b, c, d, e]
#     numbers.sort(reverse=True)
#     map(numbers, str)
#     result = "".join(numbers)
#     for i in numbers : 
#         result += str(i)
#     return int(result)


 

# 핵심은 동작 계산을 잘 정해주는 것. 로직을 짜는 것. 







# 별 찍기2
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다. 
# 함수 이름 : print_ stars2
# 출력 결과 
"""
   *
  **
 ***
****
"""


def print_stars2(n):
    for i in range(1, n+1): # 1~n
        print(" " * (n - i) + "*" * i)

print_stars2(10)

# 별찍기 10종 세트라는 게 있다...

# input output 구조 
# 저장 -> 다음에 또 쓰려고 기록장치에 저장하는 것.. 프로그램이 합니다! 
# 내 단일 컴퓨터에서 프로그램 수행 결과를 파일로 저장하는 방법...
# 로그 기록 남기거나 계산값 저장 등을 하기 위해. 
# 설정 저장 프로그램으로 읽어오는 것 가능 









