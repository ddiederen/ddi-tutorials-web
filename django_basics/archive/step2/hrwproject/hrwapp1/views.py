# Import
from django.shortcuts import render

# Create your views here.
def hrwapp1_index(request):
    context = {}
    return render(request, 'hrwapp1/hrwapp1_index.html', context=context)# -*- coding: utf-8 -*-

def hrwapp1_result(request,input1):
    context = {}
    context['input1'] = input1
    return render(request, 'hrwapp1/hrwapp1_result.html', context=context)# -*- coding: utf-8 -*-