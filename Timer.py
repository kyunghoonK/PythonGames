from math import remainder


print("지금부터 타이머 시작을 누르고 문제를 풀어보세요.")
second = int(input("문제를 해결하는데 총 몇초가 걸렸나요? : "))
a = second//60
b = second%60
c = a//60
d = a%60

print(f"총 {c}시간 {d}분 {b}초만에 문제를 해결하셨습니다.")
