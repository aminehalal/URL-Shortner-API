from django.urls import path 
from . import views

urlpatterns = [
    path('get_all_urls' ,views.get_all_urls , name='get_all_url'),
    path('get_url/<str:code>' ,views.get_url_by_id , name='get_url'),
    path('url', views.url , name='url') 
]