from django.urls import path
from . import views
 

urlpatterns = [
     path('', views.index, name="index"),
     path('project_index', views.project_index, name="project_index"),
     path('about', views.about, name="about"),
     path('contact', views.contact, name="contact"),
     path('<int:pk>/', views.project_detail, name="project_detail"),
      
]