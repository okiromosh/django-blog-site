from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout')
]