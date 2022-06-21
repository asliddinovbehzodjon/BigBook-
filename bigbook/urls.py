from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="BigBook API",
      default_version='v1',
      description="This is official BigBook API.Creator : www.behzodasliddinov.uz",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="behzodme@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,

)
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/',include('books.urls')),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)