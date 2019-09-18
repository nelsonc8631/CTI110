""" This program calculates the total amount of a meal purchased
at a restaurant"""
#9/16/2019
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Christopher Nelson
"""User will enter the cost of the meal, the amount they would like to tip in
deciamal form, and the tax and this code will calculate the tip, tax, and
total meal""" 

mealCost = float(input(" Enter meal cost "))

serverTip = float(input("Enter tip for server in decimal form "))

mealTax = float(input("Enter the tax amount is decimal form "))

calTip = mealCost*serverTip

calTax = (mealCost*mealTax)

totalCost = (mealCost+ calTip+calTax)

print("Calculated tip is $ ", format(calTip, '.2f'))

print("Calculated tax is $ ",format(calTax, '.2f'))

print("Total meal cost is $ ", format (totalCost, '.2f'))

input()
                        
                        
