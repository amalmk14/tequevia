from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('',views.Home,name="home"),
    path('nav',views.Nav,name="navbar"),
    path('signin/',views.Signin,name="signin"),
    path('cart/',views.Cart,name="cart"),
    path('wishlist/',views.Wishlist,name="wishlist"),
    path('checkout/',views.Checkout,name="checkout"),
    path('order-summary',views.OrderSummary,name="oder-summary"),
    path('details/',views.Details,name="product_details"),
    path('lists/',views.Lists,name="product_lists"),
    path('footer/',views.Footer,name="footer"),
    path('privacy-policy',views.PrivacyPolicy,name="privacy-policy"),
    path('terms-conditions',views.TermsConditions,name="terms-conditions"),
    path("return-policy",views.ReturnPolicy,name="return-policy"),
    path("shipping-delivery",views.ShippingDelivery,name="shipping-delivery"),
]