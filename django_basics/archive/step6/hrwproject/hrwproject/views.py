# Import
from django.shortcuts import render

# REST imports
from hrwapp1.models import Record
from rest_framework import viewsets
from rest_framework import permissions
from hrwproject.serializers import RecordSerializer
from hrwproject.permissions import IsOwnerOrReadOnly

# Create your views here.
def home(request):
    context = {}
    return render(request, 'hrwproject/hrwproject_index.html', context=context)# -*- coding: utf-8 -*-



# REST viewset
class RecordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)