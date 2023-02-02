from django.urls import path
from ussd import views

urlpatterns = [
    path('', views.UssdView.as_view(), name='ussd'),
]