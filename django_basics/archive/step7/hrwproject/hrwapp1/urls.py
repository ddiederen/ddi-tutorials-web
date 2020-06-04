# Import
from django.urls import path
from hrwapp1 import views

# map imports
from djgeojson.views import GeoJSONLayerView
from hrwapp1.models import Record

# URLs
urlpatterns = [
    path('', views.hrwapp1_index, name='hrwapp1_index'),
    path('result/<str:input1>/', views.hrwapp1_result, name="hrwapp1_result"),
    path('taskrequest/', views.hrwapp1_taskrequest, name="hrwapp1_taskrequest"),
    path('hrwapp1_taskresult/<str:task_id>/', views.hrwapp1_taskresult, name="hrwapp1_taskresult"),
    path('figure/<str:input1>/', views.hrwapp1_figure, name="hrwapp1_figure"),
    path('map1/', views.hrwapp1_map1, name="hrwapp1_map1"),
    path('map2/', views.hrwapp1_map2, name="hrwapp1_map2"),
    path('data/', GeoJSONLayerView.as_view(model=Record, properties=('django_id', 'room_type', 'name', 'price')),name='data'),          # note that a view is created in this line, to load data asynchronously

]