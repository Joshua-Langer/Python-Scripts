import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
grocery_item = {} # dictionary

grocery_history = [] #list

#Variable used to check if the while loop condition is met
stop = False

while not stop:

    #Accept input of the name of the grocery item purchased.
    item_name = input("Item name:\n")
    #Accept input of the quantity of the grocery item purchased.
    quantity = input("Quantity purchased:\n")
    #Accept input of the cost of the grocery item input (this is a per-item cost).
    cost = input("Price per item:\n")
    #Using the update function to create a dictionary entry which contains the name, number and price entered by the user.
    grocery_item ={'name':item_name, 'number':int(quantity), 'price':float(cost)}
    #Debug Item Dictionary
    #print(grocery_item)
    #Add the grocery_item to the grocery_history list using the append function
    grocery_history.append(grocery_item)
    #Accept input from the user asking if they have finished entering grocery items.
    #Debug History to ensure proper input
    #print(grocery_history)
    end = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
    if end == 'q':
        stop = True
        

# Define variable to hold grand total called 'grand_total'
grand_total = 0
#Define a 'for' loop.  
for grocery_item in grocery_history:
  #Calculate the total cost for the grocery_item.
  item_total = grocery_item['number'] * grocery_item['price']
  #Debug item costs
  #print(item_total)
  #Add the item_total to the grand_total
  grand_total = grand_total + item_total
  #Debug Grand Total
  #print(grand_total)
  #Output the information for the grocery item to match this example:
  #2 apple	@	$1.49	ea	$2.98
  print(str(grocery_item['number']) + ' ' + str(grocery_item['name']) + '  @  ' + '$'+ str(grocery_item['price']) + '  ea  ' + str(item_total))
  #Set the item_total equal to 0
  item_total = 0


#Print the grand total
print("Grand total: " + " "+ str(locale.currency(grand_total, grouping = True)))
