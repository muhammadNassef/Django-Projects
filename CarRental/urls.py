from django.urls import path
from . import views

app_name = 'CarRental'
urlpatterns = [
    path('', views.CarRentalIndexView, name='CarRentalIndexView'),
    path('welcomeS/', views.signupView, name='signupView'),
    path('welcomeL/', views.logInView, name='logInView'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("password_reset_confirm/", views.password_reset_confirm, name="password_reset_confirm"),
]
