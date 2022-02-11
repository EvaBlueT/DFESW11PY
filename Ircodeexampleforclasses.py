def lettertest(invar):
    if invar.upper() in "AEIOUY":
        return True
    else: 
        return False

def verticalsym(invar):
    if invar.upper() in "AHIMOTUVWXY":
        return True
    else:
        return False

var1 = input("Enter Letter: ")
var2 = lettertest(var1)
if var2:
    print(var1 + " is a vowel")
else:
    print(var1 + " is a consonant")

var3 = verticalsym(var1)
if var2:
    print(var1 + " has a vertical symetry")
else:
    print(var1 + " does not have a vertical symetry")
