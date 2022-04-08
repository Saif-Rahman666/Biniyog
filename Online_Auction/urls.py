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
    
    path('bidding_status', Bidding_Status, name='bidding_status'),
    path('bidding_status2', Bidding_Status2, name='bidding_status2'),
    path('result', result, name='result'),
    path('edit_profile',Edit_Profile,name="edit_profile"),
    path('edit_profile1',Edit_Profile1,name="edit_profile1"),
    path('change_password',Change_Password,name="change_password"),
    path('change_password1',Change_Password1,name="change_password1"),
    path('admin_home', Admin_Home,name="admin_home"),
    path('add_product', Add_Product,name="add_product"),
    path('new_product', New_product,name="new_product"),
    path('seller_user', Seller_User,name="seller_user"),
    path('all_product', All_product, name='all_product'),
    path('all_product2', All_product2,name="all_product2"),
    path('profile', profile, name='profile'),
    path('profile1', Profile1, name='profile1'),
    path('view_auction(<int:pid>)', view_auction, name='view_auction'),
    path('start_auction(<int:pid>)', Start_Auction, name='start_auction'),
    path('view_category', view_category, name='view_category'),
    path('feedback', Feedback,name="feedback"),
    path('view_feedback', view_feedback, name='view_feedback'),
    path('view_subcategory', view_subcategory, name='view_subcategory'),
    path('view_session_date', view_session_date, name='view_session_date'),
    path('view_session_time', view_session_time, name='view_session_time'),
    path('status(<int:pid>)', Change_status, name='status'),
    path('add_category', Add_Category, name='add_category'),
    path('add_subcategory', Add_SubCategory, name='add_subcategory'),
    path('add_session_date', Add_Session_date, name='add_session_date'),
    path('add_session_time', Add_Session_time, name='add_session_time'),
    path('Member_Payment_mode', Member_Payment_mode, name='Member_Payment_mode'),
    path('Member_Google_pay', Member_Google_pay, name='Member_Google_pay'),
    path('load-courses/', load_courses, name='ajax_load_courses'),
    path('load-courses1/', load_courses1, name='ajax_load_courses1'),
]
