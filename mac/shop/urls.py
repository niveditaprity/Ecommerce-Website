from django.urls import path
from . import views


urlpatterns =[
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("productview/",views.ProductView,name="ProductView"),
    path("checkout/",views.Checkout,name="Checkout"),
    path("register/",views.Register,name="Register"),
    path("login/",views.Login,name="login"),
    path("cart/",views.Cart,name="Cart"),
    path("orders/",views.Orders,name="Orders"),
    path("userprofile/",views.UserProfile,name="UserProfile"),
]