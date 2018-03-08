## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(x):
    x=abs(int(x))
    if x < 2:
        return False
    if x % 2 == 0:
        return False
    if x > 2:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True



#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(h):
    p=0
    while p<h:
        p=p+1
        if h%p==0:
            print p
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(n):
    lorgest = 0
    n=int(n)
    for i in range (n+1):
        if is_prime(i):
            largest = i

    return largest
#### End OF MARKER



if __name__ == '__main__':
    print is_prime(499)  # should return True

    print get_largest_prime(10)  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
