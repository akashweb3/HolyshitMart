from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('aboutus', views.about, name='AboutUs'),
    path('contactus', views.contact, name='Contactus'),
    path('tracker', views.tracker, name='TrackingStatus'),
    path('search', views.search, name='Search'),
    path('productview', views.ProdView, name='ProductView'),
    path('checkout', views.checkout, name='Checkout'),

]
