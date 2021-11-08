from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json
import datetime
from . utils import cookieCart,cartData

# Create your views here.
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    # order = data['order']    
    # items = data['items']

    products = Product. objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']    
    items = data['items']

    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)
 
def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']    
    items = data['items']

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

 