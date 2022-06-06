// console.log("Hello ji static...")
var updateBtns = document.getElementsByClassName("update-cart")

for(i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productID=this.dataset.product
        var action = this.dataset.action
        console.log("productId:",productID," Action:",action)

        console.log("User:",user)
        if(user == "AnonymousUser"){
            // console.log("User not authenticated")
            addCookieItem(productID, action)
        }
        else{
             updateUserOrder(productID,action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('Not logged in....')

    if(action=='add'){
        if(cart[productId] == undefined){
            cart[productId] ={'quantity': 1}
        }
        else{
            cart[productId]['quantity'] += 1
        }
    }
    if(action == 'remove'){
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity'] <= 0 ){
            console.log('Item should be deleted || Remove Item')
            
            //----------------------------------------------------------------------------------------------------
            //in project this delete operator is used
            delete cart[productId]; 
            //delete is a javascript operator            
            /* The JavaScript delete operator removes a property from an object;
             if no more references to the same property are held, it is eventually released automatically. */
            /* delete operator leaves undefine value for the deleted property 
            (which will give and error if we remove an item from cart for guest user by clicking the down arrow) */
            //----------------------------------------------------------------------------------------------------
            
            //----------------------------------------------------------------------------------------------------
            //online idea :: stackoverflow
            // const {productId, ...cartWithoutDeletedPdt} = cart;
            // cart = cartWithoutDeletedPdt;
<<<<<<< HEAD
=======
            
>>>>>>> temp
            // console.log(cartWithoutDeletedPdt )
            //----------------------------------------------------------------------------------------------------
        }
    }

    console.log('Cart: ', cart)
    document.cookie =  'cart=' + JSON.stringify(cart) + ";domain=;path=/"

    // location.reload() //earlier it was this 
    document.location.reload() //this resolved the negative cart error for unauthenticated/guest user

    //without this I had to refresh after each change to see the updated data on site
    //there are better ways to do this (as on large scale this would make the site slow)


}

function updateUserOrder(productID,action){
    console.log("User is authenticated,sending data ... ")

    var url ="/update_item/"

    fetch(url,{
        method:"POST",
        headers:{
            'Content-Type':"application/json",
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({"productId":productID,"action":action}),
    })
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
        console.log("Data:",data)
        location.reload() //this was there earlier
        // document.location.reload()
        
    });
    //forgot the semi-colon


} 