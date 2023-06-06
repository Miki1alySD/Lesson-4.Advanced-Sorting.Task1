# 1. Вывод бинарного представления числа:


def get_bin(b: int, res=-1):
    if b == 0:
        return 0
    res += 1
    return (b % 10) * (1 << res) + get_bin(b // 10, res)

print(get_bin(1101))


#Умножение:

def tmp(n, m, s=0) :
    m = str(m)
    if len(m) == 1 :
        return int(str(s) + '0') + fun(n, int(m))
    else :
        s = int(str(s) + '0') + fun(n, int(m[0]))
        return tmp(n, m[1:],s)
 
def fun(a, b) :
    if not b :
        return 0
    return a + fun(a, b-1)
 
x, y = map(int, input('введите числа через пробел: ').split())
 
print(tmp(x, y))


# Возведение в степень:

def exponentiation(N, p):
    if p == 0:
        return 1
    return N * exponentiation(N, p-1)

no = int(input('введите число которое хотите возвести в степень: '))
nt = int(input('введите число которое будет степенью в которую возводите: '))
 
print(exponentiation(no, nt))