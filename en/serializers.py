from rest_framework import serializers
from .models import EnLangWord

class EnLangWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnLangWord
        fields = ('word',)
