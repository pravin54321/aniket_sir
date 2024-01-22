from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PaymentStatus(APIView):
    def get(self,request,*args, **kwargs):
        payment_id=kwargs.get('id')
        return Response({'id':payment_id},status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serialiser=PaymentStatusSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'msg':'data save successfully'},status=status.HTTP_200_OK)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)
