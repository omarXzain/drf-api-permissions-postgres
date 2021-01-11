from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .serializer import DigimonSerializer
from .models import Digimon

# Create your views here.
class DigimonListView(ListAPIView):
    queryset = Digimon.objects.all()
    serializer_class = DigimonSerializer

class DigimonDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Digimon.objects.all()
    serializer_class = DigimonSerializer