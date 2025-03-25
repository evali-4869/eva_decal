#1. 
#(1) pwd
#(2) ls
#(3) cd ../brianna_repo
#    git pull origin main
#(4) mv homework.py ~/python_decal/judy_decal/homework/
#(5) cat homework.py
#(6) nano homework.py
#(7) git add homework.py
#    git commit -m "add hw"
#    git push origin main
#(8) git pull origin main
#   there's updates in the remote repository that my local repository does not have
#(9) cd ~/recent/
#2.
#(2.1)
def checkDataType(x):
    return type(x)
print(checkDataType(3.14))
print(checkDataType(True))
#(2.2)
def evenOrOdd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOrOdd(7))
print(evenOrOdd(10))
#3.
def sumWithLoop(numbers):
    x = 0
    for i in range(len(numbers)):
        x += numbers[i]
    return x
print(sumWithLoop(numbers = [1, 2, 3, 4, 5]))
#4.
#4.1
def duplicateList(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i)
        new_lst.append(i)
    return new_lst
print(duplicateList(["a", "b", "c"]))
#4.2
#def square(num):
#   return num * num