from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('page/', views.page, name='page'),
    path('post/', views.post, name='post'),

]
