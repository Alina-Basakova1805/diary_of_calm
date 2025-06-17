from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_wiew, name='register'),
    path('login/', views.login_wiev, name='login'),
    path('logout/', views.logout_wiew, name='logout'),
]