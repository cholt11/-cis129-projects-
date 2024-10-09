# Moduel 4   
# CARSON HOLT 
# 10/09/2024
#This program calculates store and employee bonuses based on monthly sales and sales increases 


# declare local variables 
monthlySales = 0 # monthy sales amount 
storeamount = 0 # store bonus amount 
empAmount = 0 # employee bonus amount 
salesIncrease = 0 # percent of sales increase 
prompt = "Enter the monthly sales amount: " # prompt will be a string literal 

# This code gets the monthy sales amount 
monthlySales = float(input(prompt))

# This code determines the storeamount bonus 
if monthlySales >= 110000:
  storeAmount = 6000
elif monthlySales >= 100000:
  storeAmount = 5000
elif monthlySales >= 90000: 
  storeAmount = 4000
elif monthlySales >= 80000:
  storeAmount = 3000
else:
  storeAmount = 0 

# This code gets the increase in sales percentage 
salesIncrease = float(input("Enter the sales increase in decimal format: ") 
salesincrease = salesIncrease / 100

# This code determines the empAmount bonus 
if salesIncrease >= .05:
  empAmount = 75 
elif salesIncrease >= .04:
  empAmount = 50
elif salesIncrease >= .03:
  empAmount = 40
else: 
  empAmount = 0 

# This code prints the bonus info 
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount) 
if (storeamount == 6000) and (empAmount ==75):
  print('CONGRATS! YOU HAVE REACHED THE HIGHEST BONUS POSSIBLE!')
