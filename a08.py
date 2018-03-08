## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results):
    lst=[]
    if results == None:
        return None
    for k in results:
        for l in k[0:1]:
            for m in k[1:2]:
                lst.append(tuple((l,m,sm((k)))))

    return lst
def sm(res):
   # for i in results:
    add=0
    for j in res :
        #if type(i)==None or type(j)==None:
        if type(j) == None:
            add=add+0
        elif type(j)==int or type(j)==float:
            add=add+j
    return add




#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(results):
    listoftuples=find_cumulative_marks(results)
    lst1=[]
    newlist = []
    tuple = ()
    for i in listoftuples:
        value = (i[2])
        tuple = value

        newlist += [tuple]
        newlist.sort(reverse=True)
    highest = newlist[0]
    result = highest

    for i in listoftuples:
        for k in i[2:]:
            if k==result:
                lst1.append(i[0:2])
    return lst1
                    #return i[0:2]


#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print find_cumulative_marks(results)
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('p101111', 'Ali Khayam')
