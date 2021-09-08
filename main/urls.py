from django.contrib import admin
from django.urls import path


from .views import index,about,base, list_page
app_name='main'

urlpatterns = [
    path('', index, name='index_page'),
    path('about/', about, name='about_page'),
    path('base/', base, name='base_page'),
    path('wisher/<int:pk>/', list_page, name='wish_list_page'),
]