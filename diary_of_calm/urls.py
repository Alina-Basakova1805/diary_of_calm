from . import views
from django.urls import path
# python3 manage.py runserver 7643

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('entries/',views.my_entries, name='my_entries'),
    path('create/',views.create_entry,name = 'create_entry')]