# Import
from django.urls import path
from hrwapp1 import views

# URLs
urlpatterns = [
    path('', views.hrwapp1_index, name='hrwapp1_index'),
    path('result/<str:input1>/', views.hrwapp1_result, name="hrwapp1_result"),
    path('taskrequest/', views.hrwapp1_taskrequest, name="hrwapp1_taskrequest"),
    path('hrwapp1_taskresult/<str:task_id>/', views.hrwapp1_taskresult, name="hrwapp1_taskresult"),
]