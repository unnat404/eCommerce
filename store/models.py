from django.db import models
from django.contrib.auth.models import User
from django.utils import translation #in-built model in django
# import Pillow

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    # test_var=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=7,decimal_places=2) 
    #max price of an item can have 7 decimal places => max_price<=1000000.00
    digital=models.BooleanField(default=False,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    # complete=models.BooleanField(default=False,null=True,blank=False)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()        
        cart_total=sum([item.get_total for item in orderitems])
        return cart_total

    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()        
        item_total=sum([item.quantity for item in orderitems])
        return item_total

    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping = True
                break # this is added by UNNAT seperately, to save some time
        return shipping 

        
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    # one product can have multiple orderItems
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank =True)
    # quantity=abs((int)(quantity)) #want to make quantity to be +ve always
    date_added=models.DateTimeField(auto_now_add=True)

    @property 
    def get_total(self):
        total=self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    zip_code=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address



