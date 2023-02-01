from django.urls import path
from ussd.views import UssdView

urlpatterns = [
    path('', UssdView.as_view(), name='ussd'),
]