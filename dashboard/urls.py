from django.urls import path

from dashboard import views
from dashboard import therapist
from dashboard import psychiatrist
from dashboard import mh_provider
from dashboard import resource

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/index.html', views.index , name='index'),
    path('users/', views.index, name='index'),
    path('dashboard/', views.home, name='home'),
    path('login/', views.user_login, name='login'), 
    path('logout/', views.user_logout, name='logout'), 
    path('admin_users/', views.admin_users, name='admin_user'),
    path('admin_users/add/', views.add_admin_user, name='add_admin_user'),
    path('admin_users/edit/<int:user_id>/', views.edit_admin_user, name='edit_admin_user'),
    path('admin_users/delete/<int:user_id>/', views.delete_admin_user, name='delete_admin_user'),
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
    path('resources/', resource.resource_page, name='resources'),
    path('resources/add/', resource.resource_add, name='add_resource'),
    path('resources/edit/<int:resource_id>/', resource.resource_edit, name='edit_resource'),
    path('resources/delete/<int:resource_id>/', resource.resource_delete, name='delete_resource'),
]