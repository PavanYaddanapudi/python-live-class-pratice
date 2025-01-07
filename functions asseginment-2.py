def discount_decider(price,quantity):
    if quantity>10:
        price = price*quantity
        discounted_price = price-(price*(10/100))
        return discounted_price
    else:
        return -1
 

price = float(input('enter price per item:'))
quantity = int(input('enter quantity:'))

bill = discount_decider(price,quantity)
if bill==-1:
    print('No discount applied :(. \nFinal Bill:',price*quantity)
else:
    print('10% discount applied :). \nFinal Bill:',bill)
