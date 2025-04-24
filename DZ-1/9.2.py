def rem(n: int,m: int,b: int ) -> int:
    if m == 0:
        return 1
    elif m%2==0:
        return rem(n*n % b, m//2, b)
    else:
        return n*rem(n*n % b, (m-1)//2, b) % b
    
    
# print(15**(2**16+1)%123)
# print(rem(15, 2**16+1, 123))

print(rem(3,5,7))
print(3**5 % 7)