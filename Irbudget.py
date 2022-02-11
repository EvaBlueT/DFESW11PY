# Create a Budget class that can instantiate objects based on different budget
#  categories like food, clothing, and entertainment. 
# These objects should allow for depositing and withdrawing funds 
# from each category, as well computing category balances 
# and transferring balance amounts between categories

class Budget:
    balancelist = []

    def balancetest(self, invar):
        if invar >= 10:
            return "there is still enough money"
        elif invar < 10 and invar > 1:
            return "there is a little money"
        else:
            return "there is not enough money"

food = Budget()

print(food.balancelist)
print (food.balancetest(int(input("What is your food balance?: "))))

clothing = Budget()

print(clothing.balancelist)
print(clothing.balancetest(int(input("What is your clothing balance?: "))))


