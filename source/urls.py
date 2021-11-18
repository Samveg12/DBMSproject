from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name = "source/login.html")),
    path('logout', auth_views.LogoutView.as_view(template_name = "source/logout.html")),
    path('create',views.Create.as_view()),
    path('all',views.All.as_view()),
    path('accounts/',include('allauth.urls')),
    path('change/<int:pk>',views.updates.as_view()),
    path('delete/<int:pk>',views.deletes.as_view()),
    path('update/<int:pk>',views.updates.as_view()),
]

