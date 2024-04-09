#Carly's Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

print("Welcome to Carly's Clippers!")

#Calculating Total Price
total_price = 0
for i in prices:
 total_price += i

#Average price
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

#New Price
new_prices = [new - 5 for new in prices]
print("Updated prices:", new_prices)

#Total Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue:", total_revenue)

#Average Daily Revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue is:", average_daily_revenue)

#Haircuts Under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30 ]
print("All hairstyles under $30:", cuts_under_30)