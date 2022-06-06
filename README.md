
# eCommerce
 
A fully functional eCommerce website with guest user checkout capabilities.

# Project Features:
    • Guest User Checkout functionality with Cookies
    • Products can be Physical(shipping required) or Digital(no shipping required)  
    • Payment Integration
    • Order Summary before payment

--------------------    
# Setup and Run Locally:
1. Clone the repo
2. Set up a virtual environment with requiements.txt
3. Change directory to:  ecommerce
4. Create superuser (optional) 
    `python manage.py createsuperuser `
5. Make migrations and migrate to setup database :
    ` python manage.py makemigrations` 
    `python manage.py migrate `
6. Run the following commands in terminal:
    ` python manage.py process_tasks `
    ` python manage.py runserver `
7. Visit http://127.0.0.1:8000/<endpoint> to view different end-points metioned below


--------------------

# Test Endpoints
## Home Page
![image](https://user-images.githubusercontent.com/53619178/147363247-52655be4-ecff-459c-bc5e-dda5dac31ba7.png)

## Cart Page
![image](https://user-images.githubusercontent.com/53619178/147363434-cd0bf4c7-6cb0-45e9-b3a4-e0bef4d80446.png)


## Checkout Page
![image](https://user-images.githubusercontent.com/53619178/147363491-ba87dcc9-c1ee-4739-8b90-8aa027a67242.png)


## Info & Payment Section
![image](https://user-images.githubusercontent.com/53619178/147363297-c1b07def-285a-4130-a041-63295badcf11.png)
![image](https://user-images.githubusercontent.com/53619178/147363306-f913dd40-0d51-4d76-aeca-b635ad343636.png)


--------------------

