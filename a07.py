## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###

def calculate_sgpa(lst):
    total_marks = 0
    total_number_of_subject = 0
    s=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
    if lst == None:
        return None
    if type(lst) != list:
        if lst != 'nothing':
            total_number_of_subject = total_number_of_subject + 1
            total_marks = total_marks + variable(lst)
    if type(lst) ==list:
        for i in lst:
            if i not in s:
                return None
    if type(lst) == list:
        for x in lst:
            if  x != 'nothing':
                total_number_of_subject = total_number_of_subject + 1
                total_marks = total_marks + variable(x)


    if total_number_of_subject == 0:
        return 0
    sgpa = total_marks / total_number_of_subject
    return sgpa

def variable(grades):
    if grades == "A+":
        return 4.00
    elif grades == "A" :
        return 4.00
    elif grades == "A-" :
        return 3.67
    elif grades == "B+" :
        return 3.33
    elif  grades == "B" :
        return 3.00
    elif  grades == "B-" :
        return 2.67
    elif  grades == "C+" :
        return 2.33
    elif  grades == "C" :
        return 2.00
    elif  grades == "C-" :
        return 1.67
    elif  grades == "D+" :
        return 1.33
    elif   grades == "D" :
        return 1.00
    elif grades == "F":
        return 0.00



#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(a,b):
    g=[]
    w=[]
    p=[]
    mul=[]
    s=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
    if type(a) != list:
        g.append(a)
    else:
        for i in a:
            g.append(i)
    if type(b) != list:
        w.append(b)
    if type(b) == list:
        for j in b:
            w.append(j)
    for i in g:
        if i not in s:
            return None
    if len(g) != len(w):
        return None
    if g == None :
        return None
    for i in g[0:]:
        p.append(variable(i))
    if type(p) == None:
        return None
    for j in range(0,len(p)):
        mul.append((p[j]) * (w[j]))
    x=sum(mul)
    y=sum(w)
    if y == 0:
        return None
    sgpa=x/y
    return sgpa


    #if len(lst1) != len(lst2):
    #    return None



#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa(['A+'])
    print calculate_sgpa_weighted(['A+'], [4])
