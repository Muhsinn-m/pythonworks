prices={'carrot':100,'orange':150,'apple':200}

discount_rate=0.15

discount_prices={item:prices*(1-discount_rate) for item,prices in prices.items()}

print(discount_prices)

