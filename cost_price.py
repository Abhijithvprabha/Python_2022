cost_price = int(input("Enter the cost of the bike? "))
road_tax = 0
if cost_price > 100000:
    road_tax= cost_price * .12
elif cost_price > 50000 and cost_price <= 100000 :
    road_tax = cost_price * .1
else:
    road_tax = cost_price * .04
print(f"The road tax to be paid is ${road_tax}")

