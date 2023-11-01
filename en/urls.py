from django.urls import path
from .views import EnLangWordView

urlpatterns = [
    path('api/en/random', EnLangWordView.as_view(), name='en')
]
