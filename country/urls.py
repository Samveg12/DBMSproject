from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index.as_view(),name="countryHome"),
    path('country/<int:id>', views.country,name="country"),
    path('country/disasterdisplay/<int:pk>', views.Disaster.as_view(),name="disaster"),
    path('register',views.register)
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

