from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('search/',views.search,name='search'),
    path('productview/',views.productview,name='productview'),
    path('tracker/',views.tracker,name='tracker'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('about',views.about,name='about')
]
