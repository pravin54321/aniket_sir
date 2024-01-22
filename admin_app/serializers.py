from rest_framework import serializers
from .models import *

class PaymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=PyamentStatusModel
        fields='__all__'