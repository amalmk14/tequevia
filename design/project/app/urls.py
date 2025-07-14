from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('',views.Home,name="home"),
    path('cart/',views.Cart,name="cart"),
    path('cart2/',views.Cart2,name="cart2"),
    path('wishlist/',views.Wishlist,name="wishlist"),
    path('checkout/',views.Checkout,name="checkout"),
    path('order-summary',views.OrderSummary,name="oder-summary"),
    path('details/',views.Details,name="product_details"),
    path('details2/',views.Details2,name="product_details2"),
    path('list/',views.List,name="product_list"),
    path('list2/',views.List2,name="product_list2"),
]