fruits=['apple','banana','orange']

prices=[159,110,60]

fruit_price={fruits[i]:prices[i] for i in range(len(fruits))}
print(fruit_price)