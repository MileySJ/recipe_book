from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('asian/', views.asian, name='asian'),
    path('italian/', views.italian, name='italian')
]
