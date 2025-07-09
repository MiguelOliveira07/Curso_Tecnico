min_food = 50
min_drinks = 75
min_clean = 30

name_product = input("What is the name of product? ")
category = input("What is the category? [food, drink, cleaning] ")
amount_stocked = int(input("How many do you have on your storage? "))

if category == 'food':
    if amount_stocked <= min_food:
        print(f'You need to buy more {name_product}, your storage have just {amount_stocked} {name_product}, is amost over...')

if category == 'drink':
    if amount_stocked <= min_drinks:
        print(f'You need to buy more {name_product}, your storage have just {amount_stocked} {name_product}, is amost over...')

if category == 'cleaning':
    if amount_stocked <= min_clean:
        print(f'You need to buy more {name_product}, your storage have just {amount_stocked} {name_product}, is amost over...')   
