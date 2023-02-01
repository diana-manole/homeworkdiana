
from django.urls import path

from . import views

app_name = 'finapp'

urlpatterns = [
    #HomePage
    path('', views.index, name='index'),
    
    path('year', views.year, name='year'),
    path('year/<int:year_id>', views.year, name='year'),
    
     path('month', views.month, name='month'),
    path('month/<int:month_id>', views.month, name='month'),
    
     path('business', views.business, name='business'),
    path('business/<int:business_id>', views.business, name='business')]
