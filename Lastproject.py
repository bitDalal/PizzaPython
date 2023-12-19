global total
def order_pizza():
    list=[]
    list2=[]
    invoice=[]
    total=0
    addtoppingscost=0
    num=eval(input('\nHow many pizza you want? '))
    i=num
    for i in range(num):
        type1=input('\nPepperoni (P), Margherita (M), Vegetarian (V), Neapolitan (N)\n  Pizza type: ')
        invoice.append(type1)
        size=input('\nLarge (L), Medium (M), Small (S) \n  Enter pizza size: ')
        invoice.append(size)
        if size=="L" or size=="l":
            total=total+50
        elif size=="M" or size=="m":
            total=total+40
        elif size=="S" or size=="s":
            total=total+30


        topping=print('\nAdd toppings to your pizza.\n Olives (O), Tomatoes (T), Mushrooms (M), Jalapenos (J)')
        topping=input('\nAdd topping 1 to your pizza\n add:')
        list.append(topping)
        topping=input('\nAdd topping 2 to your pizza\n add:')
        list.append(topping)
        topping=input('\nAdd topping 3 to your pizza\n add:')
        list.append(topping)
        addtoppings=input('\nAdd extra toppings to your pizza? Yes or No? ')
        if addtoppings=="Yes" or addtoppings=="yes":
            addtoppings=eval(input('\nHow many topping you want to add?'))
            for i in range (addtoppings):
                addExtratoppings=input('Add topping to your pizza\n Olives (O), Tomatoes (T), Mushrooms (M), Jalapenos (J).\n add:')
                list2.append(addExtratoppings)
                addtoppingscost= addtoppings * 3
        else:
            addtoppings=="No" or addtoppings=="no"
            
    print('\n-----------------  Invoice  -----------------')
    print('Pizza' '\t\t\tSize' '\t\t\tPrice' '\t\t\tToppings' '\t\t\tExtra Toppings')
    i=num
    print(invoice)
    for i in range(num):
        if (type1=='P' or type1=='p') and (size=='L' or size=='l'):
            print("Pepperoni Pizza  \tLarge  \t\t\t50 \t\t\t", list,  list2, addtoppingscost)
        if (type1=='P' or type1=='p') and (size=='M' or size=='m'):
            print("Pepperoni Pizza  \tMedium  \t\t\t40 \t\t\t", list,  list2, addtoppingscost)
        if (type1=='P' or type1=='p') and (size=='S' or size=='s'):
            print("Pepperoni Pizza  \tSmall  \t\t\t30 \t\t\t", list,  list2, addtoppingscost)

        if (type1=='M' or type1=='m') and (size=='L' or size=='l'):
            print("Margherita Pizza  \tLarge  \t\t\t50 \t\t\t", list,  list2, addtoppingscost)
        if (type1=='M' or type1=='m') and (size=='M' or size=='m'):
            print("Margherita Pizza  \tMedium  \t\t\t40 \t\t\t", list,  list2, addtoppingscost)
        if (type1=='M' or type1=='m') and (size=='S' or size=='s'):
            print("Margherita Pizza  \tSmall  \t\t\t30 \t\t\t", list,  list2, addtoppingscost)
                    
        if (type1=='V' or type1=='v') and (size=='L' or size=='l'):
            print("Vegetarian Pizza  \tLarge \t\t\t50 \t\t\t", list,  list2, addtoppingscost)
        if (type1=='V' or type1=='v') and (size=='M' or size=='m'):
            print("Vegetarian Pizza  \tMedium \t\t\t40 \t\t\t", list,  list2, addtoppingscost)
        if (type1=='V' or type1=='v') and (size=='S' or size=='s'):
            print("Vegetarian Pizza  \tSmall \t\t\t30 \t\t\t", list,  list2, addtoppingscost)

        if (type1=='N' or type1=='n') and (size=='L' or size=='l'):
            print("Neapolitan Pizza  \tLarge \t\t\t50 \t\t\t", list,  list2, addtoppingscost)
        if (type1=='N' or type1=='n') and (size=='M' or size=='m'):
            print("Neapolitan Pizza  \tMedium \t\t\t40 \t\t\t", list,  list2, addtoppingscost)
        if (type1=='N' or type1=='n') and (size=='S' or size=='s'):
            print("Neapolitan Pizza  \tSmall \t\t\t30 \t\t\t", list,  list2, addtoppingscost)

    print('\n\nYour total payment is ', total, 'with extra toppings ', addtoppingscost+total)
    

def display_page():
    print ('\nA.Pizza Menu')
    print ('B.Ordar Pizza')
    print ('C.Exit\n')


def menu_list():
    print('\nMenu')
    
    Pepperoni=['Pepperoni Pizza   Large   50AED\nPepperoni Pizza   Medium   40AED\nPepperoni Pizza    Small    30AED']

    Margherita=['\nMargherita Pizza   Large   50AED\nMargherita Pizza   Medium   40AED\nMargherita Pizza   Small   30AED']

    Vegetarian=['\nVegetarian Pizza   Large   50AED\nVegetarian Pizza   Medium   40AED\nVegetarian Pizza   Small   30AED']

    Neapolitan=['\nNeapolitan Pizza   Large   50AED\nNeapolitan Pizza   Medium   40AED\nNeapolitan Pizza   Small   30AED']
#The join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator.
    print(' '.join(map(str, Pepperoni)))
    print(' '.join(map(str, Margherita)))
    print(' '.join(map(str, Vegetarian)))
    print(' '.join(map(str, Neapolitan)))

        
print ('Welcome')

while True:
    display_page()
    choes=input('Select an option:')
    
    if choes=="A" or choes=="a":
        menu_list()
        
    elif choes=="B" or choes=="b":
        order_pizza()
        
    elif choes=="C" or choes=="c":
        print('Thank you for visiting us!')
        break
