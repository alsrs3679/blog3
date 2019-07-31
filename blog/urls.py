from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('new/', views.new, name ="new"),
    path('create/', views.create, name ="create"),
    path('<int:blog_id>/', views.detail, name = "detail"),
]