## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def is_prime1(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
def output_prime_factors(num):
    num=round(num)
    p=0
    while p < num:
        p +=1
        if num % p==0 and is_prime1(p)==True:
            print p

#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def is_prime(num):
    f=2
    while (f < num):
        if num % f ==0:
            return False
        f=f+1
    return True
def get_nth_prime(n):
    if type(n)==float:
        print None
    if n==1:
        return 2
    x=1
    num =3
    while (x<=n):
        if is_prime(num):
            x=x+1
            if x == n:
                return num
        num=num+2



#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(23)
    print get_nth_prime(4)
