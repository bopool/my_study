# 2 ~ 9 사이의 숫자를 입력받아
# 해당하는 단의 구구단을 출력하세요. 
# 2 ~ 9 사이의 숫자가 아닌 값이 입력된 경우, 
# "잘못 입력되었다고 출력"하고 
# "다시 입력" 받으세요.

# if문 input for문 

# nn = int(input("몇 단을 원하시나요? "))
# print("----------")
# if nn >= 2 and nn <= 9:
#     for a in range(1, 10):
#         print(nn,"*", a, "=", nn*a)
# else:
#     print("잘못 입력하셨습니다.")
# print("----------")


# n = int(input("몇 단? "))
# while not 2 <= n <= 9: # while not : 조건이 True면 그만 반복하고 다음 줄로 내려감. false면 안의 내용을 실행한다.  
#     print("2 ~ 9 사이의 숫자를 입력해 주세요.")
#     n = int(input("몇 단? "))

# print("----------")
# for i in range(1, 10):
#     print(n, "*", i, "=", n*i)
# print("----------")



#    이터러블 



# 
# if nn > 2 and nn > 9:
#    pass

# 
# if nn >= 2 and nn <= 9:
#    구구단출력


# python에서만 
# if nn >= 2 and nn <= 9:
# if 2 <= nn >= 9




# 정수를 입력받고 
# 그 정수보다 작은 수 중 
# 가장 큰 제곱수를 출력하세요. 
# 입력하는 수는 2 이상

# n = int(input("숫자를 입력하세요."))
# i = 1
# while True:
#     if i ** 2 >= n:
#         break
#     oo = i ** 2
#     i += 1
# print(oo)



# [1, 2, 3, 4, 5]
# [10, 20, 30, 40, 50]
# [532, 5941, 54682, 58, 5]
# 3개의 리스트에서 같은 인덱스의 값끼리 더하여 출력하세요. 

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40, 50]
# c = [532, 5941, 54682, 58, 5]

# for i in range(5): 
#     print(a[i] + b[i] + c[i])

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40, 50]
# c = [532, 5941, 54682, 58, 5]
# i = 0 
# while i < 5:
#     print(a[i] + b[i] + c[i])
#     i += 1 


# zip()
# 길이가 같은 list를 묶어서 for문 등으로 사용가능한 iterable을 반환한다. 
# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40, 50]
# c = [532, 5941, 54682, 58, 5]
# for x, y, z in zip(a, b, c):
#     print(x + y + z)
#     print(x, y, z)


    
# 정수를 입력받고 
# 1부터 입력받은 정수까지 모두 출력하세요. 
# 단, 숫자에 3, 6, 9가 들어있는 경우 숫자 대신 짝 이라고 출력하세요. 

# n = int(input("숫자를 입력하세요. "))
# for i in range(1, n + 1):
#     # 3, 6, 9가 들어 있으면
#     # 931 --> "931" 
#     answer = i 
#     for j in str(i):
#         if int(j) % 3 == 0 and j != "0": 
#             answer = "짝"
#             break
#     print(answer) 





# 적당히 쌓이면 열심히 한 게 된다. 감당 가능한 선에서 진행하세요. 
# 다양한 방법이 있어요!

# 힌트
# "3", "6", "9"
# 931 // 100
# 931 % 100
# 31 // 10 == (931 % 100) // 10



# 나머지가 
# 각 자리수의 숫자를 확인해야 함





# i = int(input("숫자를 입력하세요."))
# n = 1

# while (n ** 2) > i > 2:
#     print(n ** 2)
#     n += 1
    
# 1/2 == 0.5
# 4 ** 1/2 == 2 == 4 ** 0.5




# 정수를 입력받고 그 정수의 약수를 모두 출력하세요. 
# 약수 : 나누었을 때 나머지가 0으로 나누어 떨어지게 하는 수 

# n = int(input("약수구하기 : "))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)


# n = int(input("약수구하기 : "))
# for i in range(n):
#     a = n + 1
#     if n % (i+1) == 0:
#       print(i)


# n = int(input("약수구하기 : "))
# i = 1 
# while i <= n:
#     if n % i == 0:
#         print(i)
#     i += 1

# import copy
# a = [5, 4, 3, 2, 1]
# b = copy.deepcopy(a)

# print(id(a), id(b))

a == 10
b == 10
a == b