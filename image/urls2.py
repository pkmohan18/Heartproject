from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="login"),
    path('register',views.register,name="register"),
    path('login',views.index,name='login'),
    path('heart_failure',views.failure,name="failure"),
    path('find_anamoly',views.find_anamoly,name="anomaly"),
    path("login",views.logout,name="logout"),
    path("home",views.home,name="home")
]
