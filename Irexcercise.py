word1 = "Good"
word2 = "Day"
word3 = "Ewa"

sentence = word1 + " " + word2 + " " + word3

print(sentence)

# number exercise

number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)


# # an improved number version:

number1 = int(input("Enter the whole number: "))
number2 = float(input("Enter a decimal number: "))
number3 = round(number2)
print(f"This a whole numer: {number1}, this is a decimal number: {number2} and this is a round decimal number {number3}")

# Pet excercise

name = "Mr Cat"
age = 7
meow = True
tweet = False

print(f"My pet is called {name} and he is {age} years old")
print(f"Statement: {name} meows. {meow}")
print(f"Statement: {name} tweets. {tweet}")
