## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x,guess=0.1):
    if x==0:
        return None
    if (guess * guess)-x<0.00001 and (guess * guess)-x > 0:
        return guess
    else:
        new_guess =improve_guess(guess,x)
        return sqrt(x,new_guess)

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(a,b):
	average =(a + b)/2.0
	return average

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess,x):
    new_guess=average(guess,x/guess)
    return new_guess


#### End OF MARKER




if __name__ == '__main__':
    print sqrt(36)
