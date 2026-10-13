str1 = "chips"
int1 = 10
float1 = 1.50
bool1 = False
print(type(str1))
packetprice=float(input("packetprice:"))
quantity=int(input("quantity:"))
itemtotal=packetprice*quantity
print("total price of the item is",itemtotal)
quantity=int(input("stock of chips left :"))
if quantity < 5:
    print("is chips restock needed:yes")
else:
    print("is chips restock needed:no")
a=10
b=12
temp=a
a=b
b=temp
print("after swpping:",a,b)
shop_name = "quick" + " " + "bites"
print("shop name:", shop_name)
print("letter in shop name:", len(shop_name))
print("first letter:", shop_name[0])