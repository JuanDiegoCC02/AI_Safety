from django.shortcuts import render
from rest_framework import generics

from .models import ModerationResult
from .serializers import ModerationResultSerializer

# Create your views here.

class ModerationResultListCreateView(
    generics.ListCreateAPIView
):
    queryset = ModerationResult.objects.all()
    serializer_class = ModerationResultSerializer