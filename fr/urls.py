from django.urls import path
from .views import FrLangWordView

urlpatterns = [
    path('api/fr/random/', FrLangWordView.as_view(), name='fr')
]
