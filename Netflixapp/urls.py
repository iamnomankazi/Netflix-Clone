from django.urls import path, include
from .views import DeleteUser, Home, Infopage, UserDataTable, UserUpdate, View, landingpage, signup, login, watchpage

urlpatterns = [
    path('home/', Home, name = 'Home'),
    path('home/<int:pk>/<str:cat>', View, name='View'),
    path('home/signup', signup, name='signup'),
    path('home/login', login, name='login'),
    path('', landingpage, name='landingpage'),
    path('home/watch', watchpage, name='watchpage'),
    path('home/show/users', UserDataTable, name='UserDataTable'),
    path('home/show/users/<int:pk>', DeleteUser, name='DeleteUser'),
    path('home/show/users/<int:pk>', UserUpdate, name='UserUpdate'),
    path('about/', Infopage, name='About')
]
