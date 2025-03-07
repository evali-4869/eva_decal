#2.1 Making a List Variable
numbers = []
for i in range(21):
    numbers.append(i)
print(numbers)
#TypeError: 'builtin_function_or_method' object is not subscriptable
#I changed .append[] to parentheses instead of square brackets

#2.2 Working with List Elements
def squareList():
    squ_num = []
    for j in range(len(numbers)):
        squ_num.append(pow(numbers[j], 2))
    return squ_num
print(squareList())
#SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
# I accidentally called the new list instead of the function, changed print(squ_num) to print(squareList)
#Also changed squ_num.append(j)=pow(numbers[j], 2) to squ_num.append(pow(numbers[j], 2))

#2.3 Slicing
def sub_squarelist(list):
    squ_num = list
    sub_squ = squ_num[0 : 15]
    return sub_squ
print(sub_squarelist(squareList()))
# I counted one more in the slicing, chcanged [0:16] to [0:15]

#2.5 Slicing & Striding
def anotherlist(list):
    sub_num = list
    sec_num = sub_num[::-3]
    return sec_num
print(anotherlist(squareList()))

#3.1 Creating a 5x5 2D List
def create_2d_list():
    matrix = []
    x = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(x)
            x +=1
        matrix.append(row)
    return matrix
print(create_2d_list())

#3.2 Replacing 2D List with Multiples of 3
def modified_2d_list(matrix):
    new_matrix = []
    for i in range(5):
        row = matrix[i]
        for j in range(5):
            if row[j] % 3 == 0:
                row[j] = "?"
        new_matrix.append(row)
    return new_matrix
print(modified_2d_list(create_2d_list()))

#3.3 Summing None-’ ?’ Elements
def sum_non_question_elements(new_matrix):
    sum_num = 0
    for i in range(5):
        row = new_matrix[i]
        for j in range(5):
            if row[j] != '?':
                sum_num += row[j]
    return sum_num
print(sum_non_question_elements(modified_2d_list(create_2d_list())))
                
            
        
