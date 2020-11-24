from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('addstocks',views.addstocks,name='addstocks'),
    path('delete/<stock_id>',views.delete,name='delete'),
    path('delete_stock',views.delete_stock,name='delete_stock'),

]