from django.shortcuts import render

# Create your views here.

def Signin(request):
    return render(request,"dummylogin.html")

def Home(request):
    return render(request,"home.html")

def Cart(request):
    return render(request,"cart.html") 

def Cart2(request):
    return render(request,"cart2.html") 

def Wishlist(request):
    return render(request,"wishlist.html")

def Checkout(request):
    return render(request,"checkout-new.html")

def OrderSummary(request):
    return render(request,"order-summary.html")

def Details(request):
    return render(request,"product_details.html")

def List(request):
    return render(request,"product_list.html")

def List2(request):
    return render(request,"product_list2.html")
