from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from auction.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('trainer_home',Auction_User,name="trainer_home"),
    path('login_user',Login_User,name="login_user"),
    path('about',About,name="about"),
    path('logout', Logout, name="logout"),
    path('login_admin',Login_Admin,name="login_admin"),
    path('signup', Signup_User,name="signup"),

   
]
