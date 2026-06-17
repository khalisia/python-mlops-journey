products = ["Book", "Pen", "Laptop"]
prices = [500, 50, 80000]
categories = zip(products,prices)

for index,category in enumerate(categories):
    print(index,category)