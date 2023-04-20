# dictionary(딕셔너리) 자료형
# 이름표를 달아서 찾을 수 있도록 해 놓은 것
# key-value 형태
# key: value
# value나 key 자리에 list, 숫자, 문자 등 여러 타입의 값이 들어갈 수 있다. 
# key 값으로 검색한다. 

person = {
    "이름": "김땡땡", 
    "나이": 18, 
    "점수": {
        "영어": 80, 
        "국어": 90, 
        "수학":80
        }
}
print(person["나이"]) # 18 출력
print(person["점수"]) # {'영어': 80, '국어': 90, '수학': 80} 출력
print(person["점수"]["영어"]) # 80 출력


# dictionary에 정보 추가하는 방법 
dict_1 = {1: 'a'}
dict_1['b'] = 2 # dict_1 변수에 'b': 2 추가하겠다. 
dict_1[1] = 'c' # 1 이라는 키에 해당하는 value 재할당 방법 {1: 'c', 'b': 2} 로 바뀌었다.
del dict_1[1] # {'b': 2} 1 이라는 key값에 해당하는 정보가 삭제됨
print(dict_1)



dict_2 = {1:'a', 2:'b', 3:'c'}
# keys()
## dictionary에서 key 값만 리스트 형태로 돌려준다.
dict_keys = dict_2.keys()
print(dict_keys)

# values()
## dictionary에서 value 값만 리스트 형태로 돌려준다. 
dict_values = dict_2.values()
print(dict_values)

# items()
## dictionary에서의 key-value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
dict_items = dict_2.items()
print(dict_items) 


# get()
# key에 대응되는 value를 돌려준다. 
# key 값이 존재하지 않으면 None을 돌려준다. 
# 값이 None일 경우, 뒤에 표기해 준 값으로 출력해 줌 (숫자, 문자, 기타 등등)
# dictionary에서 없는 key나 value를 호출하면 에러가 남
# dict_2["나이"] # KeyError: '나이'
print(dict_2.get("나이", "나이 불명")) # 에러 대신 None (의미있는 것은 없다는 값이)이 호출됨


# clear()
## 딕셔너리 안의 모든 요소를 삭제한다. 
dict_2.clear()
print(dict_2)
