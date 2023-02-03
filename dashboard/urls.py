from django.urls import path

from dashboard import views
from dashboard import therapist
from dashboard import psychiatrist
from dashboard import mh_provider

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
    path('psychiatrists/', psychiatrist.psychiatrist_page, name='psychiatrists'),
    path('psychiatrists/add/', psychiatrist.add_psychiatrist, name='add_psychiatrist'),
    path('psychiatrists/edit/<int:psychiatrist_id>/', psychiatrist.edit_psychiatrist, name='edit_psychiatrist'),
    path('psychiatrists/delete/<int:psychiatrist_id>/', psychiatrist.delete_psychiatrist, name='delete_psychiatrist'),
    path('providers/', mh_provider.mental_health_provider_page, name='providers'),
    path('providers/add/', mh_provider.add_provider, name='add_provider'),
    path('providers/edit/<int:provider_id>/', mh_provider.edit_provider, name='edit_provider'),
    path('providers/delete/<int:provider_id>/', mh_provider.delete_provider, name='delete_provider'),
]