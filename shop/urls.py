from django.urls import path
from .import views

urlpatterns = [
    


    path("", views.index, name="ShopHome"),
    path('login', views.loginUser,name='login'),
    path('signup/', views.signupUser,name='signup'),
 
    path('logout/', views.handleLogout, name='handleLogout'),

    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("prodView/<int:myid>", views.prodView, name="prodView"),
    path("checkout/", views.checkout, name="Checkout"),

    # path('login', views.handleLogin, name='handleLogin'),
    # path('signup', views.handleSignup, name='handleSignup'),

    path('logout/', views.handleLogout, name='handleLogout'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]



