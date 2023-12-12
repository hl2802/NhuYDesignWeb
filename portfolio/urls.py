from django.urls import path
from . import views
app_name= 'portfolio'
urlpatterns = [
    path('', views.index, name='portfolio'),
    path('<int:id>', views.single_portfolio, name='single_portfolio'),
]