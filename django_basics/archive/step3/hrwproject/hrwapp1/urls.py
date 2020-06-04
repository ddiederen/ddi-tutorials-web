# Import
from django.urls import path
from hrwapp1 import views

# URLs
urlpatterns = [
    path('', views.hrwapp1_index, name='hrwapp1_index'),
    path('result/<str:input1>/', views.hrwapp1_result, name="hrwapp1_result"),
]