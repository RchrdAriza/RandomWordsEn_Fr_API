from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EnLangWord
import random
from .serializers import EnLangWordSerializer

# Create your views here.


class EnLangWordView(APIView):
    def get(self, request):
        words = EnLangWord.objects.all()

        if words:
            word_random = random.choice(words)
            serializer = EnLangWordSerializer(word_random)
            return Response(serializer.data)
        else:
            return Response({
                'message': 'there was an error'
            })

def home(request):
    return render(request, 'home.html')
