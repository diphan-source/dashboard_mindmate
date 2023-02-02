from django.urls import path

from dashboard import views
from dashboard import therapist

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.home, name='home'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='logout'), 
    path('therapists/', therapist.therapist_page, name='therapists'),
    path('therapists/add/', therapist.add_therapist, name='add_therapist'),
    path('therapists/edit/<int:therapist_id>/', therapist.edit_therapist, name='edit_therapist'),
    path('therapists/delete/<int:therapist_id>/', therapist.delete_therapist, name='delete_therapist'),
    path('therapists/details/<int:therapist_id>/', therapist.therapist_details, name='therapist_details'),
]