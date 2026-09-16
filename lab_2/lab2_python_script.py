# Question 1: multiply all numbers in list
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
result1 = 1
for i in part1:
    result1 *= i
print("Question 1 Result: ", result1)

# Question 2: add all numbers in list
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result2 = 0
for i in part2:
    result2 += i
print("Question 2 Result: ", result2)

# Question 3: add only even numbers in list
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]
result3 = 0
for i in part3:
    if i % 2 == 0:
        result3 += i
print("Question 3 Result: ", result3)