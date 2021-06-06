from .models import Ecomweb,Searchquery
from rest_framework import serializers

class EcomwebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecomweb
        fields = ['id','name','country','website']

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searchquery
        fields = ['id','name','date','search_type']