## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(FinalGrad):
    if FinalGrad >= 90 and FinalGrad <= 100:
        return("A+")
    elif FinalGrad >=86 and FinalGrad <= 90:
        return("A")
    elif FinalGrad >=82 and FinalGrad <= 86:
        return("A-")
    elif FinalGrad >=78 and FinalGrad <= 82:
        return("B+")
    elif FinalGrad >=74 and FinalGrad <= 78:
        return("B")
    elif FinalGrad >=70 and FinalGrad <= 74:
        return("B-")
    elif FinalGrad >=66 and FinalGrad <= 70:
        return("C+")
    elif FinalGrad >=62 and FinalGrad <= 66:
        return("C")
    elif FinalGrad >=58  and FinalGrad <= 62:
        return("C-")
    elif FinalGrad >=54 and FinalGrad <= 58:
        return("D+")
    elif FinalGrad >=50 and FinalGrad <= 54:
        return("D")
    else:
        return("F")
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####


def calculate_sgpa(grade1,grade2,grade3):
    grade1=input()
    grade2=input()
    grade3=input()
    total_marks=4.00
    total_number_of_subjects=0

    if grade1 != 0:
        total_number_of_subjects=total_number_of_subjects + 1
        total_marks = total_marks + calculate_sgpa(grade1)
    if grade2!=0:
        total_number_of_subjects=total_number_of_subjects + 1
        total_marks = total_marks + variable(grade2)
    if grade3!=0:
        total_number_of_subjects=total_number_of_subjects + 1
        total_marks = total_marks + variable(grade3)
    if total_number_subjects==0:
        return 0
    sgpa = total_marks / total_number_of_subjects
    return sgpa






def calculate_sgpa(grade):
    points = 0
    if grade == 'A+' :
        points +=  4.0
    if grade=='A':
        points += 4.0
    if grade == 'B+' :
        points += 3.67
    if grede =='B':
        points += 3.33
    if grade =='B-':
        points += 3.00
    if grade =='C+':
        points += 2.67
    if grade == 'C':
        points += 2.0
    if grade =='C-':
        points += 1.67
    if grade =='D+' :
        points += 1.33
    if grade == 'D' :
        points += 1.00
    if grade =='F':
        points +=0.00
#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
