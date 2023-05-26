from django.contrib import admin
from django.urls import path
from blog.views import BlogViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="MrPrezAtambaev Blog API",
        default_version="v1",
        description="API Documentation for Blog App",
        contact=openapi.Contact(email="akyl182003@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog',
         BlogViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/blog/<int:pk>/', BlogViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]