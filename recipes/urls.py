from django.urls import path, include
from . import views
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('asian/', views.asian, name='asian'),
    path('italian/', views.italian, name='italian'),
    path('asian/<int:asian_id>', views.asian_detail, name='asian_detail'),
    path('italian/<int:italian_id>', views.italian_detail, name='italian_detail'),
    path('about/', views.about, name='about'),
    path('research/', views.research, name='research'),
    path('recipe/', views.recipe, name='recipe'),

]
