""" This program will calculate the annual profit based on total sales for
the user
#9/18/2019
#CTI-110 P2T1 - Sales Predicition
# Christopher Nelson
#Input the total sales
#Calculate the profit as 23 percent of total sales
#Display the profit"""

#Get tje projected total sales
totalSales= float (input("Enter the projected number of sales "))

#Calculate the profit as 23 percent of total sales
profit = totalSales * 0.23

print("The profit is $", format (profit, ',.2f'))
