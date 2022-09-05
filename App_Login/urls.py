from unicodedata import name
from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/',views.Sign_up,name='signup'),
    path('login/',views.Login_Page,name='login'),
    path('logout/',views.Logout_Page,name='logout'),
    path('change-profile/',views.user_profile,name='change_profile')
    
]
