from django.urls import path
from . import views #para importar del directorio actual otro archivo

urlpatterns = [
    path('', views.contact, name="contact"),
]
