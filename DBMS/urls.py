from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('country.urls')),
    path('source/',include('source.urls'))
]
