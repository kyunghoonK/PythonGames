def percentage(a, b):
    return a/b * 100

a = int(input("현재 값은 = "))
b = int(input("전체 값은 = "))
c = percentage(a,b)
d = "현재 {0}% 진행중".format(c)

print(d)