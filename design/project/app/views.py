from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"home.html")

def Checkout(request):
    return render(request,"checkout.html") 

def Cart(request):
    return render(request,"cart.html") 

def Cart2(request):
    return render(request,"cart2.html") 

def Wishlist(request):
    return render(request,"wishlist.html")

def Details(request):
    return render(request,"product_details.html")

def Details2(request):
    return render(request,"product_details2.html")

def List(request):
    return render(request,"product_list.html")

def List2(request):
    return render(request,"product_list2.html")
