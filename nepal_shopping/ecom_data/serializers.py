from .models import Ecomweb
from rest_framework import serializers

class EcomwebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecomweb
        fields = ['id','name','country','website']