from django.urls import path
from . import views #para importar del directorio actual otro archivo

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
]