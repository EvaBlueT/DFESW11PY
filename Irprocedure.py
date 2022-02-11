# def vehsprint(inputvar):
#     vehvar = inputvar  + " likes fast vehicles"
#     return  vehvar

# print(vehsprint(input("What is your name?: ")))

# Tutorial on Functions

# def add_num(number1, number2):
#     answer = number1 + number2
#     return answer

# added_num = add_num(5,5)
# print(added_num + 20)

# Function Excercise
# create a program that works out a grade based on marks with the use of functions


def grade_score(home_score, asses_score, final_exam_score):
    grade = round((home_score + asses_score + final_exam_score)/175*100)
    return grade

var1 = int(input("Homework score /25: "))

var2 = int(input("Assesment score /50: "))

var3 = int(input("Final exam score /100: "))

var4 = str(input("Student Name: "))

var5 = str("%")

student_scores = grade_score(var1,var2,var3)
print(var4, + student_scores, var5)