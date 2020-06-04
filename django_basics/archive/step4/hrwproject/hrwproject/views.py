# Import
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'hrwproject/hrwproject_index.html', context=context)# -*- coding: utf-8 -*-