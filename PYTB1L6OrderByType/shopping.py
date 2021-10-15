groceryList = ["Milk", "Cheese", "Sausage", "Soup"]
shoppingCart = ["Milk", "Cheese"]
while(groceryList != shoppingCart):
    print("Continue Shopping")
    x = input("Add to your cart: ")
    shoppingCart.append(x)
print("Done shopping")