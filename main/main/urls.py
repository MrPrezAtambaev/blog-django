from django.contrib import admin
from django.urls import path
from blog.views import BlogViewSet
from main.yasg import urlpatterns as docs_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog',
         BlogViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/blog/<int:pk>/', BlogViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

urlpatterns += docs_url