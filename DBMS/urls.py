from django.contrib import admin
from django.urls import path,include

import source
from . import views
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('country.urls')),
    path('source/',include('source.urls')),
    path('api/detail/',include('source.api.urls','api_detail')) ,
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
