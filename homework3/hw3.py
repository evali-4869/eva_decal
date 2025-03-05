#1. Oski Stole Your Power
def power(x, y):
    z = 1
    for i in range(y):
        z *= x
    return z
print(power(2,3))

#2 What Should I Wear?
def temp(readings = []):
    return (min(readings), max(readings))
print(temp(readings = [15, 14, 17, 20, 23, 28, 20]))

#3 Check if its the Weekend
def isWeekend(x):
    if x == 6 or 7:
        print(True)
    else:
        print(False)
print(isWeekend(6))

#4 Fuel Efficiency Calculator
def fuel_efficiency(distance, fuel):
    return distance / fuel
print(fuel_efficiency(70, 21.5))

#5 Secret Code
def decodeNumbers(n):
    if n < 10:
        print(n)
    else:
        a = n % 10
        b = n // 10
        c = 1
        temp = b
        while temp > 0:
            c *= 10
            temp //= 10
        return a * c + b
print(decodeNumbers(12345))

#6.1 For Loops
def find_min_with_for_loop(nums):
    x = nums[0]
    for i in range(len(nums) - 1):
        if x > nums[i + 1]:
            x = nums[i + 1]
    return x
print(find_min_with_for_loop(nums = [2024, 98, 131, 2, 3, 72]))

def find_max_with_for_loop(nums):
    x = nums[0]
    for i in range(len(nums) - 1):
        if x < nums[i + 1]:
            x = nums[i + 1]
    return x
print(find_max_with_for_loop(nums = [2024, 98, 131, 2, 3, 72]))

#6.2 While Loops
def find_min_with_while_loop(nums):
    x = nums[0]
    i = 1
    while i < len(nums):
        if x > nums[i]:
            x = nums[i]
            i += 1
    return x
print(find_min_with_while_loop(nums = [2024, 98, 131, 2, 3, 72]))

def find_max_with_while_loop(nums):
    x = nums[0]
    i = 1
    while i < len(nums):
        if x < nums[i]:
            x = nums[i]
            i += 1
    return x
print(find_max_with_while_loop(nums = [2024, 98, 131, 2, 3, 72]))

#7 Counting Vowels
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    v_cnt = 0
    c_cnt = 0
    for i in text:
        if i.isalpha():
            if i in vowels:
                v_cnt += 1
            else:
                c_cnt += 1
    return (v_cnt, c_cnt)
print(vowel_and_consonant_count("UC Berkeley, founded in 1868!"))

#8 Calculate Digital Root
def digital_root(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum
print(digital_root(2468))