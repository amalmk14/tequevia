from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"home.html")

def Nav(request):
    return render(request,"navbar.html")

def Signin(request):
    return render(request,"signin.html")

def Cart(request):
    return render(request,"cart.html") 

def Wishlist(request):
    return render(request,"new-wishlist.html")

def Checkout(request):
    return render(request,"checkout-new.html")

def OrderSummary(request):
    return render(request,"order-summary.html")

def Details(request):
    return render(request,"product_details.html")

def Lists(request):
    return render(request,"lists.html")

def Footer(request):
    return render(request,"footer.html")

def PrivacyPolicy(request):
    return render(request,"privacy-policy.html")

def TermsConditions(request):
    return render(request,"terms-conditions.html")

def ReturnPolicy(request):
    return render(request,"return-policy.html")

def ShippingDelivery(request):
    return render(request,"shipping-delivery.html")

def MyAccount(request):
    return render(request,"my-account.html")

def MyOrders(request):
    return render(request,"my-orders.html")


def CheckoutSummary(request):
    return render(request,"checkot-summary.html")