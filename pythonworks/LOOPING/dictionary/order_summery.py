#order_summery

orders=["tea","coffe","tea","coffe","gheeroast","planerost","porotta","tea"]

order_count={}

for item in orders:

    if item in order_count:

        order_count[item]+=1

    else:
        order_count[item]=1

print(order_count)