from django.urls import path, include
from . import views
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('asian/', views.asian, name='asian'),
    path('italian/', views.italian, name='italian'),
    path('<int:asian_id>', views.asiandetail, name='asiandetail'),
    path('<int:italian_id>', views.italiandetail, name='italiandetail'),

]
