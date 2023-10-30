#class 
#check in a list
#help from Gumula
class CheckInput:
  @staticmethod   #decorator
  def getCorrectInput(listOfAnswers,question):
    userInput=""
    while not (userInput in listOfAnswers):
      userInput=input(question)
    #return True     -> you could return whatever data you need
    return userInput


whatsNext="another order"
subtotal=0
order=["","","","",""]
masterList=[]
discount=""

#indexes
patty_index=0
meal_index=1
dog_index=2
side_index=3
drink_index=4

#COSTS
kpPrice=1.25
kp2Price=2.00
kp3Price=3.00
scPrice=.25
cbsPrice=1.00
cbmPrice=1.25
cblPrice=1.50
krPrice=1.50
ssaucePrice=.50

kmPrice=3.50
km2Price=3.75
km3Price=4.00
ssdPrice=1.25
flPrice=2.00
ssurpPrice=3.00
glPrice=2.00
regsaucePrice=.50
ksPrice=2.00
seafoamSPrice=1.00
seafoamMPrice=1.25
seafoamLPrice=1.50


#main order process

while whatsNext=="another order":
    
    #patty
    pattyQ=CheckInput.getCorrectInput(["yes","no"],"Would you like a Krabby Patty? (yes or no):  ")
    if pattyQ=="yes":
        whatPatty=CheckInput.getCorrectInput(["s","d","t"],"Would you like a single, double, or triple? (s,d,t):  ")
        if whatPatty=="s":
            order[patty_index]="Single Krabby Patty"
            subtotal+=kpPrice
            withSeaCheese=CheckInput.getCorrectInput(["yes","no"],"Would you like sea cheese with the patty? (yes or no):  ")
            if withSeaCheese=="yes":
              subtotal += scPrice
        elif whatPatty=="d":
            order[patty_index]="Double Krabby Patty"
            subtotal+=kp2Price
            withSeaCheese=CheckInput.getCorrectInput(["yes","no"],"Would you like sea cheese with the patty? (yes or no):  ")
            if withSeaCheese=="yes":
                subtotal += scPrice
        elif whatPatty=="t":
            order[patty_index]="Double Krabby Patty"
            subtotal+=kp3Price
            withSeaCheese=CheckInput.getCorrectInput(["yes","no"],"Would you like sea cheese with the patty? (yes or no):  ")
            if withSeaCheese=="yes":
                subtotal += scPrice

          
    #krabby meal
    krabbyMealQ=CheckInput.getCorrectInput(["yes","no"],"Would you like a Krabby Patty Meal? (yes or no):  ")
    if krabbyMealQ=="yes":
        howManyPatties=CheckInput.getCorrectInput(["s","d","t"],"Would you like a single, double, or triple patty meal? (s,d,t):  ")
        if howManyPatties=="s":
            order[meal_index]="Single Krabby Patty Meal"
            subtotal+=kmPrice
        elif howManyPatties=="d":
            order[meal_index]="Double Krabby Patty Meal"
            subtotal+=km2Price
        elif howManyPatties=="t":
            order[meal_index]="Triple Krabby Patty Meal"
            subtotal+=km3Price


    #dogs
    dogsQ=CheckInput.getCorrectInput(["yes","no"],"Would you like a dog? (yes or no):  ")
    if dogsQ=="yes":
        whatDog=CheckInput.getCorrectInput(["ssd","f","ss","gl"],"Would you like a Salty Sea Dog(ssd), Footlong(f), Sailors Surprise(ss), or a Golden Loaf(gl)?  ")
        if whatDog=="ssd":
            order[dog_index]="Salty Sea Dog"
            subtotal+=ssdPrice
        elif whatDog=="f":
            order[dog_index]="Footlong"
            subtotal+=flPrice
        elif whatDog=="ss":
            order[dog_index]="Sailors Surprise"
            subtotal+=ssurpPrice
        elif whatDog=="gl":
            order[dog_index]="Golden Loaf"
            subtotal+=glPrice
            withRegularSauce=CheckInput.getCorrectInput(["yes","no"],"Would you like sauce with the golden loaf? (yes or no):  ")
            if withRegularSauce=="yes":
                subtotal += regsaucePrice

          
    #sides
    sidesQ=CheckInput.getCorrectInput(["yes","no"],"Would you like a side? (yes or no):  ")
    if sidesQ=="yes":
        whatSide=CheckInput.getCorrectInput(["cb","kr"],"Would you like coral bits or kelp rings? (cb or kr):  ")
        if whatSide=="cb":
            order[side_index]="Coral Bits"
            whatSizeCoralBits=CheckInput.getCorrectInput(["s","m","l"],"Small, medium, or large? (s,m,d):  ")
            if whatSizeCoralBits=="s":
                subtotal+=cbsPrice
            elif whatSizeCoralBits=="m":
                subtotal+=cbmPrice
            elif whatSizeCoralBits=="l":
                subtotal+=cblPrice
        elif whatSide=="kr":
            order[side_index]="Kelp Rings"
            subtotal+=krPrice
            withSaltySauce=CheckInput.getCorrectInput(["yes","no"],"Would you like salty sauce with the kelp rings? (yes or no):  ")
            if withSaltySauce=="yes":
                subtotal += ssaucePrice


    #drinks
    drinksQ=CheckInput.getCorrectInput(["yes","no"],"Would you like a drink? (yes or no):  ")
    if drinksQ=="yes":
        whatDrink=CheckInput.getCorrectInput(["ks","ss"],"Would you like a Kelp Shake or Seafoam Soda? (ks or ss):  ")
        if whatDrink=="ks":
            order[drink_index]="Kelp Shake"
            subtotal+=ksPrice
        elif whatDrink=="ss":
            order[drink_index]="Seafoam Soda"
            whatSizeSeafoamSoda=CheckInput.getCorrectInput(["s","m","l"],"What size Seafoam Soda? (s,m, or l):  ")
            if whatSizeSeafoamSoda=="s":
                subtotal+=seafoamSPrice
            elif whatSizeSeafoamSoda=="m":
                subtotal+=seafoamMPrice
            elif whatSizeSeafoamSoda=="l":
                subtotal+=seafoamLPrice
    
    #let user deicde what to do
    whatsNext==""

    #what's next?
    whatsNext=CheckInput.getCorrectInput(["another order","delete an order","edit an order","finish"],"What next? (another order), (delete an order), (edit an order), (finish) ")
    if whatsNext=="another order":
        print("New Order Requested. \n")
        masterList.append(order)

    elif whatsNext=="delete an order":
        whatIndex=int(input("What order index? (1-...)  "))
        del masterList[int(whatIndex)]
        print(masterList[int(whatIndex)])
        print("Order has been removed.")
  
    elif whatsNext=="edit an order":
        whatIndex=input("What order index? (1-...)  ")
        newMessage=input("What's the new message?  ")
        masterList[int(whatIndex)].set_message(newMessage)
  
    elif whatsNext=="finish":
        print("Final calculations being processed. \n")
        for order in masterList:
            print(f"Order {(masterList.index)+1}")
            print(patty_index)
            print(meal_index)
            print(dog_index)
            print(side_index)
            print(drink_index)
            print(f"Subtotal: ${subtotal}")
        #discount
        if (patty_index!="" or meal_index!="") and side_index=="Coral Bits" and drink_index=="Seafoam Soda":
            subtotal-=1.00
            discount="yes"
        tax=round(subtotal*.07,2)
        totalwithtax=(subtotal+tax)
        print(f"Tax: ${tax}")
        print(f"Final Amount: ${totalwithtax}")
        if discount=="yes":
            print("Discount Applied.")
