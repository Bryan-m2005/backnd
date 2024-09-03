from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina),
    path('pagina2/', views.info),
]