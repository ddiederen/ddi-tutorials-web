# Import
from django.contrib import admin
from django.urls import path, include, re_path
from hrwproject import views

# URLs
urlpatterns = [
    path('', views.home, name='home'),
    path('hrwapp1/', include('hrwapp1.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # re_path(r'^api-auth/', include('rest_framework.urls')),
    # path('schema/', schema_view),
]