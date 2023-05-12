
# students = {"보라돌이" : 61, "뚜비" : 35, "나나" : 78, "뽀" : 88}
# result = [(name,True) if score>60 else (name, False) for name,score in students.items()]

# print(result)


# print(7*2+8*4)





# import time
# start = time.time() #시작시간저장
# python_list = []
# python_list = [x**3+10 for x in python_list]
# print('time:', time.time() - start) # 현재시각-시작시간 = 실행시간 


# def func0(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for arg1 in kwargs.items():
#         print(arg1)    

# func0(10, 20, 'a',x=130, y=80, z='b')

# import numpy as np

# arr = np.arange(30).reshape(3,2,5)
# print(arr)




# import numpy as np

# arr1 = np.arange(8).reshape(2,-1)
# arr2 = np.arange(-40,40,10).reshape(2,-1)
# print(arr1)
# print(arr2)
# print("-----------------------------------------------")
# print(np.maximum(arr1,arr2)) # 같은 원소에서 가장 큰 값
# print(np.subtract(arr1,arr2)) # 뺄셈
# print(np.multiply(arr1,arr2)) # 같은 원소끼리 곱셈

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)

# func(1, 2, a=100, b=200)

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-5,5,0.5)

y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2, marker='D')
plt.plot(x, y3, color='r')
plt.plot(x, y4, linestyle = 'dashed')
plt.show()
