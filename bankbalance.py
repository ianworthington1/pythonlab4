#balance.py

def main():
    originalBalance = float(input("What was the original amount in your savings account?")) #stores originalBalance as an integer after a prompt for input from user
    interestRate = float(input("What is the percentage rate applied to your savings?")) #stores interestRate as an integer after a prompt for input from user
    timeFrame = float(input("Over how many years do you wish to apply the savings rate?")) #stores timeFrame as an integer after a prompt for input from user
    savingPeriods = float(input("How many quarters would you like to calculate savings?")) #stores savingPeriods as an integer after a prompt for input from user
    loop(originalBalance, interestRate, timeFrame, savingPeriods) #calls the loop function to be fun


def savings(originalBalance, interestRate, savingPeriods):
    print(float(originalBalance  + ((originalBalance * interestRate) * savingPeriods)))


def loop(originalBalance, interestRate, timeFrame, savingPeriods):
    increments = int(timeFrame * savingPeriods)
    for i in range(increments):
        print("Quarter: ", i+1, "\tBalance: ", (float(originalBalance  + ((originalBalance * interestRate) * savingPeriods))))


main() #runs the main() function
#Compounding yearly yields a total balance of 4660.96 after 20 years
#Compounding monthly yields a total balance of 4926.80 after 20 years