from rest_framework import serializers
from .models import FrLangWord


class FrLangWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrLangWord
        fields = ('word',)
