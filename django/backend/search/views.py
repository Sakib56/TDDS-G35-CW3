from pyexpat import model
from re import search
from urllib import request
from django.http import HttpResponse
from .serializers import SearchSerializer
from rest_framework import viewsets
from .models import Search
from django.shortcuts import render
import json

# Create your views here.
class SearchView(viewsets.ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()

def search(request):
    if request.method == 'POST':
        search_json = request.body.decode('utf-8')
        # THIS IS THE INPUT!!!
        search_term = json.loads(search_json)['search']
        # for testing, can delete
        print(search_term)
    return render(request, "search.html")
