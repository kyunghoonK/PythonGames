def SPD(a, b):
    return (a - b) // 30

W = int(input('월별 수입 = '))
F = int(input('고정 지출 = '))
c = SPD(W, F)
print('일별 사용가능 금액은 {0}원 입니다.'.format(c))
