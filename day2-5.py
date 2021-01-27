n=2
while n <=100:
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n)
    n+=1