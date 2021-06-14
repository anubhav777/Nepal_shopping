from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Ecomweb, Searchquery
from .serializers import EcomwebSerializer,SearchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .files import Web_scrapper, ObjectDetect

class Ecom_data(APIView):


    def get(self, request, format=None):
        ecom = Ecomweb.objects.all()
        serializer = EcomwebSerializer(ecom, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self,request,format = None):
        serializer = EcomwebSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ObjectView(APIView):
    def get(self,request,format=None):
        func = ObjectDetect().output()
        return Response({'data':func})


class Webscrapper(APIView):

    def get(self, request, format=None):
        name = request.META['HTPP_NAME']
        func = Web_scrapper.all_data(name)
        return Response({'data':func})


class Ecom_Data_List(APIView):

    def get_object(self,id):
        try:
            return Ecomweb.objects.get(id=id)
        except:
            pass 

    def get(self,request,id, format = None):
        ecom = self.get_object(id)
        serializer = EcomwebSerializer(ecom)
        return Response(serializer.data)

    def put(self,request,id, format = None):
        ecom = self.get_object(id)
        serializer = EcomwebSerializer(ecom,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status':'data not correct'})
    
    def delete(self,request,id, format = None):
        ecom = self.get_object(id)
        ecom.delete()
        return Response({'status':'data deleted'})

class Searchdata(APIView):

    def get(self,request, format = None):
        name = request.META['HTTP_NAME']
        print(name)
        func = Web_scrapper().all_data(name)
        return Response({'data':func})
        # search = Searchquery.objects.all()
        # serializer = SearchSerializer(search, many =True)
        # return Response(serializer.data)
    
    def post(self,request, format = None):
        serializer = SearchSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class Seachdataind(APIView):

    def get_object(self,id):
        try:
            return Searchquery.objects.get(id=id)
        except :
            pass
    def get(self,request,id, format = None):
        search = self.get_object(id)
        serializer = SearchSerializer(search)
        return Response(serializer.data)
    
    def put(self,request,id, format = None):
        search = self.get_object(id)
        serializer = SearchSerializer(search, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
    
    def delete(self,request,id, format = None):
        search = self.get_object(id)
        search.delete()
        return Response({'status':'data deleted'})
    



