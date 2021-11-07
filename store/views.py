from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer  #from tutorial (yes work)
        order,created = Order.objects.get_or_create(customer=customer,complete=False)        
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
        
    else:
        items=[]
        order={"get_cart_total":0,"get_cart_items":0, 'shipping' : False}
        cartItems=order['get_cart_items']

    products = Product. objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)

def cart(request):
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


    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)
 
def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer  #from tutorial (yes work)
        # NOTE: above code line was in the tutorial and has an alternative objects.filter(...).first() 

        # for some reason the above code also not work but adding .first() works just fine 
        # customer=Customer.objects.filter(user=request.user).first() #from stackoverflow (yes work)        
        
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
        #we are able to query child objects by : <parent_in_small_case>.<child_in_small_case>_set.all()
    else:
        items=[]
        order={"get_cart_total":0,"get_cart_items":0, 'shipping' : False}
        cartItems=order['get_cart_items']

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/checkout.html',context)
 
def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print("ProductID:",productId)
    print("Action:",action)
    

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)
    
    if action == 'add':
        orderItem.quantity=orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity=orderItem.quantity - 1
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)

def processOrder(request):
    # the next print line can be commented out ,as it for just for checking if the fetch call worked properly
    # print('Data:',request.body) # line to test post data sent in checkout.html 
    transaction_id=datetime.datetime.now().timestamp()
    data =json.loads(request.body)

    if request.user.is_authenticated:
        customer=request.user.customer
        order, created= Order.objects.get_or_create(customer=customer , complete=False)
        total=float(data['form']['total'])
        order.transaction_id = transaction_id

        if total==order.get_cart_total:
            order.complete=True
        order.save() #save the order irrespective of fact that total is equal or not
        # to keep track if th user changed anything from frontend ,OR, if there is some error on our side for future reference

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

    else:
        print('User is not logged in...')

    return JsonResponse('Payment done-dana-dan done!!',safe=False)

 