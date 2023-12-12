from django.urls import path
from . import views
app_name= 'blog'
urlpatterns = [
    path('', views.index, name='blog'),
    path('portfolio/<int:id>/', views.single_blog, name='single_blog'),
]