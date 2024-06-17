"""
Inventory Assistant
Salma Badr
"""

# This program provides a management tool for an auto parts store


# function:    count_element
# INPUT:       a list and an object
# PROCESSING:  counts the amt of times object is present in list
# OUTPUT:      an integer representing the count of the object in the list
def count_element(list, element):
    count = 0
    for i in list:
        if i == element:
            count += 1
    return count

# function:    valid_name
# INPUT:       a string (product name) and an integer representing setting
# PROCESSING:  prompts user to continue entering names until one meets all
#              criteria for validity, produces prompts/print statements
#              depending on integer setting
# OUTPUT:      a valid product name
def valid_name(new_product_name, setting):
    if setting == 1:
        prompt = "Enter a new product: "
    else:
        prompt = "Enter a new product name: "
    while new_product_name in product_names or len(new_product_name) > 15:
        if new_product_name in product_names:
            print("Sorry, we already have an item called", new_product_name, "in the inventory")
        else:
            print("Product name too long. Maximum of 15 characters")
        new_product_name = input(prompt)
    return new_product_name

# function:    valid_cost
# INPUT:       new product cost (float) and new product (string) and setting (integer)
# PROCESSING:  prompts user to continue entering product costs until one meets all
#              criteria for validity, produces prompts/print statements
#              depending on integer setting
# OUTPUT:      a valid product cost
def valid_cost(new_product_cost, new_product, setting):
    if setting == 1:
        prefix = "the unit"
    else:
        prefix = "new"
    while new_product_cost < 1 or new_product_cost >= 1000:
        if new_product_cost < 1:
            print("Invalid cost. It must be a positive number")
        else:
            print("Invalid cost. It must be less than 1,000")
        new_product_cost = float(input(f"Enter {prefix} cost for {new_product}s: "))
    return new_product_cost

# function:    valid_quantity
# INPUT:       new product quantity (integer) and new product (string) and setting (integer)
# PROCESSING:  prompts user to continue entering product quantities until one meets all
#              criteria for validity, produces prompts/print statements
#              depending on integer setting
# OUTPUT:      a valid product quantity
def valid_quantity(new_product_quantity, new_product, setting):
    if setting == 1:
        prompt = f"How many {new_product}s do we have? "
    else:
        prompt = f"Enter new quantity for {new_product}s: "
    while new_product_quantity < 1 or new_product_quantity > 999:
        if new_product_quantity < 1:
            print("Invalid quantity. It must be a positive number")
        else:
            print("Invalid quantity. It must be less than 1,000")
        new_product_quantity = int(input(prompt))
    return new_product_quantity

# function:    find_and_replace
# INPUT:       a list, object (to replace), and new object
# PROCESSING:  finds object in list and replaces with new object
# OUTPUT:      new updated list

def find_and_replace(list, object, new_object):
    for i in range(len(list)):
        if list[i] == object:
            list[i] = new_object
    return list



# initialize variables
product_names = ["spark plug", "tire", "headlight bulb"]


products = ["spark plug"] * 10 + ["tire"] * 5 + ["headlight bulb"] * 20
costs = [49.99] * 10 + [483.99] * 5 + [19.49] * 20
product_costs = [49.99, 483.99, 19.49]


# print heading
print("Welcome to the Not Your Usual Computerized Auto Store")
print("We have the smartest solution to all your problems")
print()

# prompt user to select operation
operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")

while True:
    # initialize product count
    product_count = []

    # count number of each respective product name in products
    for product_index in range(len(product_names)):
        product_count += [count_element(products, product_names[product_index])]

    # validate operation input
    while str.lower(operation) != "s" and str.lower(operation) != "l" and str.lower(operation) != "a" and str.lower(operation) != "q" and str.lower(operation) != "r" and str.lower(operation) != "t" and str.lower(operation) != "u":
        print("Invalid option, please try again")
        print()
        operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")

    # end program if user quits
    if str.lower(operation) == "q":
        print("Thanks for using our system")
        print("See you soon")
        break

    # search operation
    elif str.lower(operation) == "s":
        product = input("Enter a product name: ")
        # if product is not in inventory
        if product not in product_names:
            print(f"Sorry, we do not have any {product}s in stock")
        # if product is in inventory, indicate price and quantity
        else:
            location = product_names.index(product)
            print(f"We have {product}s in stock and they cost ${product_costs[location]} per unit")
            print(f"We currently have {product_count[location]} in stock")
        print()
        operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")
    # list operation
    elif str.lower(operation) == "l":
        print(f"{'Product':<20s}{'Price': >s}{'Quantity':>10s}")
        # print each product's name, price, and quantity
        for i in range(len(product_names)):
            product_column = f"{product_names[i]:<18s}$"
            price_column = f"{product_costs[i]:>6.2f}"
            quantity_column = f"{product_count[i]:>10d}"
            print(f"{product_column}{price_column}{quantity_column}")
        print()
        operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")

    # add operation
    elif str.lower(operation) == "a":
        # ask user for new product's name, price and quantity and validate them
        new_product_name = valid_name(input("Enter a new product: "), 1)
        new_product_cost = valid_cost(float(input(f"Enter the unit cost for {new_product_name}s: ")), new_product_name,1)
        new_product_quantity = valid_quantity(int(input(f"How many {new_product_name}s do we have? ")),new_product_name, 1)


        print(f"{new_product_quantity} {new_product_name}s, each costing ${new_product_cost:.2f}, have been added to inventory")
        # add new product info to lists accordingly
        product_names.append(new_product_name)
        product_costs.append(new_product_cost)
        products += [new_product_name] * new_product_quantity
        costs += [new_product_cost] * new_product_quantity
        print()
        operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")

    # remove operation
    elif str.lower(operation) == "r":
        # prompt user to enter product needing removal
        remove_product = input("Enter the product that you want to remove from inventory: ")
        # if product is not in inventory
        if remove_product not in product_names:
            print(f"We dont have any {remove_product}s in inventory.")
        else:
            # if product is in inventory, remove from lists accordingly
            remove_product_loc = product_names.index(remove_product)
            remove_cost = product_costs[remove_product_loc]
            for i in range(count_element(products, remove_product)):
                products.remove(remove_product)
                costs.remove(remove_cost)
            product_costs.remove(remove_cost)
            product_names.remove(remove_product)
            print(f"All {remove_product}s have been removed from inventory")
        print()
        operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")
    # update operation
    elif operation == "u":
        # prompt user to select a product to update
        update_product = input("Enter the product that you would like to update: ")
        # if product is not in inventory
        if update_product not in product_names:
            print(f"We don't have any {update_product}s in our inventory.")
            print()
            operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")

        else:
            # prompt user to select element to update
            print("(n)ame, (c)ost or (q)uantity: ")
            update_feature = input("What would you like to update? ")

            # validate input
            while str.lower(update_feature) != "n" and str.lower(update_feature) != "c" and str.lower(
                    update_feature) != "q":
                print("Invalid option")
                print("(n)ame, (c)ost or (q)uantity: ")
                update_feature = input("What would you like to update? ")


            if str.lower(update_feature) == "n":
                # prompt user to input name and validate input
                update_product_name = valid_name(input("Enter a new product name: "), 2)

                # replace all old names with new names
                product_names = find_and_replace(product_names, update_product, update_product_name)
                products = find_and_replace(products, update_product, update_product_name)
                print(f"{update_product} has been changed to {update_product_name}")
            elif str.lower(update_feature) == "c":
                # prompt user to input new cost and validate cost
                update_product_cost = valid_cost(float(input(f"Enter a new cost for {update_product}s: ")),
                                                 update_product, 2)
                cost_to_change = product_costs[product_names.index(update_product)]
                # replace all old costs with new costs
                product_costs = find_and_replace(product_costs, cost_to_change, update_product_cost)
                costs = find_and_replace(costs, cost_to_change, update_product_cost)

                print(f"The unit cost of {update_product}s has been changed to ${update_product_cost:.2f}")
            else:
                # prompt user to enter new quantity and validate input
                update_product_quantity = valid_quantity(int(input(f"Enter new quantity for {update_product}s: ")),
                                                         update_product, 2)

                quantity_to_change = product_count[product_names.index(update_product)]
                # change list to remove or add # of products accordingly
                products = products[:products.index(update_product)] + [
                    update_product] * update_product_quantity + products[
                                                                products.index(update_product) + quantity_to_change:]
                print(f"The quantity of {update_product}s in inventory has been changed to {update_product_quantity}")

            print()
            operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")
    # total operation
    else:
        # find most expensive and least expensive products
        expensive_prod = f"{product_names[product_costs.index(max(product_costs))]:<16s}"
        cheap_prod = f"{product_names[product_costs.index(min(product_costs))]:<16s}"
        # output info
        print(f"{'Most expensive product:':<29s}{expensive_prod}(${max(product_costs):,.2f})")
        print(f"{'Least expensive product:':<29s}{cheap_prod}(${min(product_costs):,.2f})")

        # count size of inventory
        inventory_value = 0
        for i in costs:
            inventory_value += i
        # output info
        print(f"Total value of all products is: ${inventory_value:,.2f}")
        print()
        operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, (t)otals) or (q)uit: ")


































