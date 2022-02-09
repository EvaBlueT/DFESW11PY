# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 

# numlst = []
# for x in range(1500, 2701,1): 
#     if (x%7 == 0) and (x%5 == 0):
#         numlst.append(x)
# print(numlst)

# # 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. 

# temp = input("Input the temerature you would like to convert: ")


# Write a Python function to find the Max of three numbers

# def maximum(var1, var2, var3):
#     The_Max = max(var1, var2, var3)
#     return The_Max

# var1 = float(input("Give the first number: "))
# var2 = float(input("Give the second number: "))
# var3 = float(input("Give the third nymber: "))
# Maximum = maximum(var1,var2,var3)
# print("Max of three numbers is: ", + Maximum)

# Write a Python function to sum all the numbers in a list

def sum(numbers):
    total = 1
    for x in numbers:
        total = total * x
    return total

print(sum((2,3,66,8,2,)))
