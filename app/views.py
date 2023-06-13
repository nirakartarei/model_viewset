from django.shortcuts import render

# Create your views here.


from app.models import *
from app.serializers import *
from rest_framework.viewsets import ModelViewSet


class MVS(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=productserializers