from rest_framework import serializers
from models import Test

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('name', 'content', 'kind')
