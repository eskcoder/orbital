import imp
from multiprocessing import context
from tkinter import SE
from wsgiref import headers
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from itemsapp import serializers


# Create your views here.

class ItemViewSet(ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['itemname','itemcatagory']
    ordering_fields = ['itemname','last_update']

    def get_serializer_context(self):
        return {'request': self.request}




 