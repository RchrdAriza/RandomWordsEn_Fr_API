from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FrLangWord
import random
from .serializers import FrLangWordSerializer

# Create your views here.


class FrLangWordView(APIView):
    def get(self, request):
        words = FrLangWord.objects.all()

        if words:
            word_random = random.choice(words)
            serializer = FrLangWordSerializer(word_random)
            return Response(serializer.data)
        else:
            return Response({
                'message': 'there was an error'
            })
