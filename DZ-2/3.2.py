# Выполнил: Маковеев Никита Владимирович.
# Дата выполнения: 24.04.2025. 
#-----------------------------------------

# Модульное возведение в степень.


def power_mod(base, exp, mod):
    if exp<=2:
        return pow(base, exp, mod)
    n = bin(exp)[2:]
    n= list(map(int, n))
    k=len(n)
    c = base**n[0]
    for i in range(1, k):
        c=(c*c) %mod
        if n[i] ==1:
            c=(c*base) % mod
    return c
#--------------------------------------------

# Вычисление наибольшего общего делителся(gcd)

def gcd(a, b):
    new_a, new_b = max(a,b), min(a,b)
    if new_b == 0:
        return new_a
    else:
        return gcd(new_a % new_b, new_b)
# ---------------------------------------
    
    
    
# Вычисление мультипликативно обратного числа

def gcd_ex(a, b):
    if a<b:
        y, x, g = gcd_ex(b,a)
        return x, y, g
    if b == 0:
        return (1, 0, a)
    else:
        y, x, g = gcd_ex(b, a % b)
        
        return (x, y - (a // b) * x, g)
print(gcd_ex(12736, 1288214))
print(-97405*12736+(963)*1288214)
def invert(a, mod):
    alpha, _, gcd = gcd_ex(a, mod)
    if gcd != 1:
        return None
    return alpha % mod
a = 123
mod = 1009
b=invert(a, mod)
print(b, (a*b)%mod)
