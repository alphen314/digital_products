from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render

from .serializer import Fileserializer , Productserializer , Catagoryserializer
from .models import File , Catagory , Product

class ProductListView(APIView):
    def get(self , request):
        products = Product.objects.all()
        serializer = Productserializer(products, many=True ,context={'request':request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = Productserializer(product,context={'request':request})
        return Response(serializer.data)


class CatagorylistView(APIView):
    def get(self,request):
        catagory= Catagory.objects.all()
        serializer = Catagoryserializer(catagory,many=True,context={'request':request})
        return Response(serializer.data)


class CatagoryDetailView(APIView):
    def get(self,request,pk):
        try:
            catagory = Catagory.objects.get(pk=pk)
        except Catagory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = Catagoryserializer(catagory,context={'request':request})
        return Response(serializer.data)


class FileListView(APIView):
    def get(self,request,product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = Fileserializer(files,many=True,context={'request':request})
        return Response(serializer.data)


class FileDetailView(APIView):
    def get(self,request,product_id,pk):
        try:
            f = File.objects.get(pk=pk,product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = Fileserializer(f,context={'requset':request})
        return Response(serializer.data)