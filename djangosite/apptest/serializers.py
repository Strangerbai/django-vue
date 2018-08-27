from rest_framework import serializers
from apptest.models import Test

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('name', 'content', 'kind')
