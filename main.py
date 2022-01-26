cost=0
discount=0
order=[]
packet_number=""

sandwich= input("Pick a Sandwich, beef ($6.25), chicken (5.25$) , tofu ($5.75), or none   ")
if sandwich == "beef":
  print("You picked beef")
  cost = cost+6.25
  discount = discount+1
  order.append("Beef Sandwhich")
if sandwich == "chicken":
  print("You picked chicken")
  cost = cost+5.25
  discount = discount+1
  order.append("Chicken Sandwhich")
if sandwich == "tofu":
  print("You picked tofu")
  cost = cost+5.75
  discount = discount+1
  order.append("Tofu Sandwhich")
if sandwich == "none":
  print("You chose no sandwich")
  order.append("No Sandwich")

drink = input("Would you like a drink?   ")
if drink == ("yes"):
  discount = discount+1
  drink_size= input("Pick a Beverage Size, large ($2.25), medium ($1.75), or small ($1.00)   ")
  if drink_size == "large":
    print("You picked large")
    cost= cost+2.25
    order.append("Large Drink")
    
  if drink_size == "medium":
    print("You picked medium")
    cost= cost+1.75
    order.append("Medium Drink")
    
  if drink_size == "small":
    print("You picked small")
    cost= cost+1.00
    order.append("Small Drink")
    
if drink ==("no"):
  print("You choose no drink")
  drink_size=("no")
  order.append("No Drink")

fries = input("Would you like fries?   ")
if fries == ("yes"):
  discount = discount+1
  fry_size =input("Pick a size of fry, large ($2.00), medium ($1.50), or small($1.00)   ") 
  if fry_size == "large":
    print ("You picked large")
    cost=cost+2.00
    order.append("Large Fry")
    
  if fry_size == "medium":
    print ("You picked medium")
    cost=cost+1.50
    order.append("Medium Fry")
   
  if fry_size == "small":
    megasize= input("Would you like to megasize your fries?  ")
    if megasize == ("yes"):
      print("You megasized!")
      cost=cost+2.00
      order.append("Large Fry")
    if megasize == ("no"):
      print ("You picked small")
      cost=cost+1.00
      order.append("Small Fry")
     
if fries == ("no"):
  print("You choose no fries")
  fry_size=("no")
  order.append("No Fry")


ketchup_packets = int(input("How many packets of ketchup would you like?   "))
cost=cost+((ketchup_packets)*(.25))
packet_number=(ketchup_packets ,"Ketchup Packets")
order.append(packet_number)

if discount ==(3):
  print("Final Order:" ,order)
  print("you get a dollar discount!")
  cost=cost-1.00
  print("Total Cost:",cost)
else:
  print("Final Order:" ,order)
  print("you do not qualify for a discount")
  print("Total Cost: ",cost)