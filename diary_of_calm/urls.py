from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('entries/',views.my_entries, name='my_entries'),
    path('create/',views.create_entry,name = 'create_entry'),
    path('delete/<int:pk>/',views.DeleteEntryView.as_view(),name='delete_entry'),
    path('update/<int:pk>/',views.UpdateEntryView.as_view(),name='update_entry'),
    ]
