# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('todoapp.urls')),
# ]



from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Second test",
        default_version='0.808',
        description="Fist test swagger",
        terms_of_service="https://www.youtube.com/watch?v=DEDXB2bAr9o&list=PLXPrA9Gm6TC1p9nmffSzaar_gp3SLh8ip&index=3",
        contact=openapi.Contact(email="#"),
        license=openapi.License(name="Hello me"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),
    path('auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
