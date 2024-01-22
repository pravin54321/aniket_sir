from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    # path(' ', admin.site.urls),
    path('payment_status/<int:id>/', PaymentStatus.as_view(), name='payment_status'),
    path('payment_status_device',PaymentStatus.as_view(),name='payment_data')
]
   
