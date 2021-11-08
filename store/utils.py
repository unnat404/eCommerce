import json 
from . models import *

# function to make the code clean in views.py
# extract all cookie ('cart') data  
def cookieCart(request):

    # try...except to prevent error if cart cookie is not created/set 
        # we initialize an empty dictionary if cart not created 
    try:
        cart = json.loads(request.COOKIES['cart'])
    except: 
        cart = {} 
        
    print('Cart:',cart)
    items=[]
    order={"get_cart_total":0,"get_cart_items":0, 'shipping' : False}
    cartItems=order['get_cart_items']

    for i in cart:
        try:    
            cartItems += cart[i]["quantity"] 

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_items'] = cart[i]['quantity']  
            order['get_cart_total'] += total

            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                    # 'digital':product.digital,
                },
                'quantity' : cart[i]["quantity"],
                'get_total' : total
            } 
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            # case 1: if product itself is removed by site from the store
            # case 2: if guest user removes an item from order then this except block save from NoneType Error
            pass

    return {'cartItems':cartItems, 'order':order, 'items':items}