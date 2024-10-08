#define the menu of Restaurant
menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,'momos':30,'samosa':10,'golgapa':40
}

print("Welocome in BABA DHABA Restaurant \U0001F600")
print("pizza: Rs40\npasta: Rs50\nburger: Rs60\nsalad: Rs70\ncoffee: Rs80\nmomos: Rs30\nsamosa: Rs10\ngolgapa: Rs40")

order_total=0

item_1=input("enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1} has been added to your order")
    
else:
    print(f"ordered item {item_1} is not avaialable yet")
    
another_order=input("do you want to another item(Yes/No)")
if another_order=="Yes":
    item_2=input("enter the name of second item=")
    order_total += menu[item_2]
    print(f"item {item_2} has been added to order")
else:
    print("order item {item_2} is not avaialable!")
    
another_order=input("do you want to another item(Yes/No)")
if another_order=="Yes":
    item_3=input("enter the name of third item=")
    order_total += menu[item_3]
    print(f"item {item_3} has been added to order")
else:
    print("order item {item_3} is not avaialable!")
    
another_order=input("do you want to another item(Yes/No)")
if another_order=="Yes":
    item_4=input("enter the name of fourth item=")
    order_total += menu[item_4]
    print(f"item {item_4} has been added to order")
else:
    print("order item {item_4} is not avaialable!")
    
another_order=input("do you want to another item(Yes/No)")
if another_order=="Yes":
    item_5=input("enter the name of second item=")
    order_total += menu[item_5]
    print(f"item {item_5} has been added to order")
else:
    print("order item {item_5} is not avaialable!")
    
print(f"the total amount of item to pay= {order_total}Rs")