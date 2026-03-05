# Tuple program for prices

prices = tuple(map(int, input("Enter prices separated by space: ").split()))

# Total number of items sold
print("Total items sold:", len(prices))

# Cheapest item
print("Cheapest price:", min(prices))

# Costliest item
max_price = max(prices)
print("Costliest price:", max_price)

# Prices in ascending order
print("Prices in ascending order:", sorted(prices))

# Number of costliest items sold
print("Number of costliest items sold:", prices.count(max_price))