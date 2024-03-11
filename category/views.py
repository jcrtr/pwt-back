from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Use
from .serializers import CategorySerializer, UseSerializer


class CategoriesList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UseList(generics.ListCreateAPIView):
    queryset = Use.objects.all()
    serializer_class = UseSerializer


class UseDetails(APIView):
    def get_object(self, slug):
        try:
            return Use.objects.get(slug=slug)
        except Use.DoesNotExist:
            raise Http404

    def get(self, request, slug):

        data = self.get_object(slug)
        serializer = UseSerializer(data)
        return Response(serializer.data)
