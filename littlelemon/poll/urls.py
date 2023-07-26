from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="poll_home"),
    path('', views.detail, name="detail"),
]