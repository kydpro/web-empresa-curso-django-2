from django.urls import path
from . import views #para importar del directorio actual otro archivo

urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
]