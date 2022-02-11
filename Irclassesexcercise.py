# write a class called 'Lettercheck'
# create an attribute called vowels and fill it with vowels

# create a method that takes a single letter 
# and checks if it is a vowel

# return true or false

# rewrite the class so you can create different objects for 
# finding if letters are members of different letter groups

# def lettertest(invar):
#     if invar in "aeiouy":
#         return True
#     else: 
#         return False



# var1 = input("Enter Letter: ")
# var2 = lettertest(var1)
# if var2:
#     print(var1 + " is a vowel")
# else:
#     print(var1 + " is a consonant")

class Lettercheck:
    letterlist = "AEIOUY"

    def lettertest(self,invar):
        if invar.upper() in self.letterlist:
            return True
        else: 
            return False

vowls = Lettercheck()


print(vowls.letterlist)
print(vowls.lettertest("a"))

vertsym = Lettercheck()
vertsym.letterlist = "AHIMOTUVWXY"
print(vertsym.letterlist)
print(vertsym.lettertest("a"))





