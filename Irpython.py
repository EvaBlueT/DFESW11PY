# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 

numlst = []
for x in range(1500, 2701,1): 
    if (x%7 == 0) and (x%5 == 0):
        numlst.append(x)
print(numlst)

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. 

temp = input("Input the temerature you would like to convert: ")
