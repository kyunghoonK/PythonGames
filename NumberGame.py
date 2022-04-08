# while문을 이용한 숫자 맞추기 게임

prompt = "틀렸습니다. 다시 시도해 보세요."
number = 0
print("숫자를 맞춰보세요. (1 이상 100 이하의 정수)")

while number != 47 :
    number = int(input("답 : "))
    if number < 47 :
        print(prompt)
        print("Hint : UP")
    if number > 47 :
        print(prompt)
        print("Hint : DOWN")
    if number == 47 :
        print("정답")