from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('friends/', views.friends, name='friends'),
    path('user/<int:id>', views.user, name='user'),
    path('user/<int:id>/add', views.addFriend, name='addFriend'),
    path('user/<int:id>/remove', views.remove, name='remove'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]
