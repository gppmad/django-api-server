# serializers.py
from rest_framework import serializers
from .models import Ram


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = ('id','value', 'um')

class RamDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = ('id',)


