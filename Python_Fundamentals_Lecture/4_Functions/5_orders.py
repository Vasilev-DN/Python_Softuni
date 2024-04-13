def calculate_total_price(product, quantity):
    prices = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}

    if product.lower() in prices:
        price_per_item = prices[product.lower()]
        total_price = price_per_item * quantity
        return total_price
    else:
        return "Invalid product"

def main():
    product = input()
    quantity = int(input())

    total_price = calculate_total_price(product, quantity)

    if isinstance(total_price, str):
        print(total_price)
    else:
        formatted_price = "{:.2f}".format(total_price)
        print(formatted_price)

if __name__ == "__main__":
    main()
