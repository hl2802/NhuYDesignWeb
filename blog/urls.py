from django.urls import path
from . import views

app_name= 'blog'
urlpatterns = [
    path('', views.index, name='blog'),
    path('single_blog/<int:id>/', views.single_blog, name='single_blog'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),

]
