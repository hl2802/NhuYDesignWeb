from django.urls import path
from . import views
app_name= 'portfolio'
urlpatterns = [
    path('', views.index, name='portfolio'),
    path('single_portfolio/', views.single_portfolio, name='single_portfolio'),
]