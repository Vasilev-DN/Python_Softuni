items_list = input().split("|")
budget = int(input())
ticket_cost = 150
clothes_limit = 50
shoes_limit = 35
accessories_limit = 20.50
bought_items = []
for every_item in items_list:
    item, price = every_item.split("->")
    price = float(price)
    if item == "Clothes":
        if price <= clothes_limit and budget >= price:
            budget -= price
            bought_items.append(price)
    elif item == "Shoes":
        if price <= shoes_limit and budget >= price:
            budget -= price
            bought_items.append(price)
    elif item == "Accessories":
        if price <= accessories_limit and budget >= price:
            budget -= price
            bought_items.append(price)
before_sale_items = sum(bought_items)
for index in range(len(bought_items)):
    bought_items[index] *= 1.4

profit = sum(bought_items) - before_sale_items
total_money = budget + sum(bought_items)
bought_items = ["%.2f" % x for x in bought_items]
print(*bought_items)
print(f"Profit: {profit:.2f}")

if total_money >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")