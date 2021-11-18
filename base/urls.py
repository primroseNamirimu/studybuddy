
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('room/<str:pk>',views.room, name='room' ),
    path('create',views.create_room,name='create_room'),
]