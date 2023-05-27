menu={'cheeseloaded':120,'vegloaded':180,'chicken':240}
add={'cheese':20,'ketchup':30,'ketchup&cheese':50}
bill=0
a=input('enter the flavour: ')
if a in menu:
    n=int(input('enter the quantity: '))
    bill=bill+menu[a]*n
    b=input('enter 1 if addon is needed: ')      
    if b=='1':
        c=input('enter the addon: ')
        if c in add:
            bill=bill+add[c]
            print(bill)
        else:
            print('addon not found')
    else:
        print(bill)
else:
    print('flavour not found')
