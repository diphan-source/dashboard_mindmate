from django.urls import path

from dashboard import views
from dashboard import therapist

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.home, name='home'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='logout'), 
    path('therapists/', therapist.therapist_page, name='therapists'),
]