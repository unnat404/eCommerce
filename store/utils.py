import json 
from . models import *

# function to make the code clean in views.py
# extract all cookie ('cart') data for unauthenticated user and send it (to views for now) 
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


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer  #from tutorial (yes work)
        # NOTE: above code line was in the tutorial and has an alternative objects.filter(...).first() 
                
        # customer=Customer.objects.filter(user=request.user) #from stackoverflow (not work)

        # for some reason the above code also not work but adding .first() works just fine 
        # customer=Customer.objects.filter(user=request.user).first() #from stackoverflow (yes work)

        # print("\n\n===================\n")
        # # to check if an attribute exists or not 
        # if hasattr(request.user, 'customer'): 
        #     print("yes exists//// ........\n")
        # else:
        #     print("NO such attribute/// ...........\n")        
        # print("\n\n===================\n")
        
        order,created = Order.objects.get_or_create(customer=customer,complete=False)        
        items=order.orderitem_set.all()
        #we are able to query child objects by : <parent_in_small_case>.<child_in_small_case>_set.all()
        cartItems=order.get_cart_items        
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems':cartItems, 'order':order, 'items':items}