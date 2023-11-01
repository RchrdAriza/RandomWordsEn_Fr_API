from django.urls import path
from .views import EnLangWordView, home

urlpatterns = [
    path('', home, name='home'),
    path('api/en/random', EnLangWordView.as_view(), name='en')
]
