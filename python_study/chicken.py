
# if money >= chicken:
#     print("치킨을 먹는다.")
#     money = money - chicken
# if money >= beer and age >= 20:
#     print("맥주를 먹는다.")
#     money = money - beer
# if money >= drink:
#     print("음료수를 먹는다.")
#     money = money - drink


# 돈 있는대로 다 사 먹으려고 함
# if money >= chicken + beer + drink and age >= 20:
#     print("치킨과 맥주와 음료수까지 먹을 수 있다.")
# elif money >= chicken + beer and age >= 20:
#     print("치킨과 맥주 또는 치킨과 음료수까지 먹을 수 있다.")
# elif money >= chicken + drink:
#     print("치킨과 음료수까지 먹을 수 있다.")
# elif money >= chicken and age >= 20:
#     print("치킨이나 맥주나 음료수를 먹을 수 있다.")
# elif money >= chicken :
#     print("치킨이나 음료수를 먹을 수 있다.")
# elif money >= beer + drink and age >= 20:
#     print("맥주와 음료수를 먹을 수 있다.")
# elif money >= beer + drink and age < 20:
#     print("음료수를 먹을 수 있다.")
# elif money >= beer and age >= 20:
#     print("맥주나 음료수를 먹을 수 있다.")
# elif money >= drink:
#     print("음료수만 먹을 수 있다.")
# else:
#     print("아무것도 못 먹는다.")

age = 20
money = 4000
chicken = 20000
beer = 10000
drink = 5000 

# 변수 money의 잔액을 기준으로 작성한 코드
# 중복 if문 들여쓸 때 계층에 유의해야 한다 
# 돈이 많으면 모든 메뉴를 먹고 음료수 두개 먹음..
if money >= chicken:
    print("치킨을 먹는다.")
    if money - chicken >= beer and age >= 20:
        print("맥주를 먹는다.")
        if money - chicken - beer >= drink:
            print("음료수를 먹는다.")
    if money - chicken >= drink:
        print("음료수를 먹는다.")
elif money >= beer and age >= 20:
    print("맥주를 먹는다.")
    if money - beer >= drink:
        print("음료수를 먹는다")
elif money >= drink:
    print("음료수를 먹는다.")
else:
    print("다음에 온다.")