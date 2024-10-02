# cis129_Lab03_coffeeShop.py
# Author: Carson Holt 
#Date: 9/30/2024
# Purpose: This program simulates a coffee shop, where the user inputs the number of coffee and muffins are sold 
# Sales tax is calcualted as well. Giving the total.

# Constants for tax rate and prices and updated menu
COFFEE_PRICE = 5.00
MUFFIN_PRICE = 4.00 
LATTE_PRICE = 7.50
SCONE_PRICE = 3.75
TAX_RATE = 0.06

# User input for coffee and muffin orders 
print("**********************************")
print("My Coffee and Muffin Shop") 
coffees = int(input("Number of coffee ordered?"))
muffins = int(input("Number of muffin ordered?"))
lattes = int(input("Number of latte ordered?"))
scones = int(input("Number of scone ordered?"))
print("***********************************")

#Calculate the sales tax as well as the total and subtotal 
subtotal = (coffees * COFFEE_PRICE) + (muffins * MUFFIN_PRICE) + (lattes * LATTE_PRICE) + (scones   * SCONE_PRICE)
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display the receipt ( sales tax + total of muffins and coffee ) 
print("********************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{coffees} Coffees at $ {COFFEE_PRICE:.2f} each: $ {coffees * COFFEE_PRICE:.2f}")
print(f"{muffins} Muffins at $ {MUFFIN_PRICE:.2f} each $ {muffins * MUFFIN_PRICE:.2f}")
print(f"{lattes}  Lattes at $ {LATTE_PRICE:.2f} each $ {lattes * LATTE_PRICE:.2f}")
print(f"{scones} Scones at $ { SCONE_PRICE:.2f} each $ {scones * SCONE_PRICE:.2f}")
print(f"6% tax: $ {tax:.2f}")
print("--------")
print(f"Total: $ {total:.2f}")
print(" THANK YOU FOR YOUR BUISNESS ") 
print(" NEXT ORDER 50% OFF " ) 
print("********************************")

