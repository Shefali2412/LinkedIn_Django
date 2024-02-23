# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('member/', views.member_list, name='member_list'),  # Updated URL for member_list
    path('profile/<str:username>/', views.view_profile, name='view_profile'),
]
