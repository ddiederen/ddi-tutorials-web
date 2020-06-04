# Import
from django.contrib import admin
from django.urls import path, include, re_path
from hrwproject import views

# REST stuff
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
router = DefaultRouter() # Create a router and register our viewsets with it.
router.register(r'records', views.RecordViewSet)


# URLs
urlpatterns = [
    path('', views.home, name='home'),
    path('hrwapp1/', include('hrwapp1.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('schema/', get_schema_view(title="hrwproject", description="API for hrwproject", version="1.0.1"),name='hrwproject_schema'),
    path('', include(router.urls)),
]