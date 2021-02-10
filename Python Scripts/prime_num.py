def prime_num(num):
    if num<= 1:
        return num
    for i in range(2, num):
        if num% i == 0:
            return  '{} is not a prime number'.format(num)
        else:
            return '{} is a prime number'.format(num)
        
for i in range(6):
    print(prime_num(i))
