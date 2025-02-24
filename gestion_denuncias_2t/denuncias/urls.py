
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='denuncias.index'),
    # path('lista_denuncias/', views.logout, name="denuncias.lista_denuncias"),
    # path('crear_denuncia/',  views.logout, name="denuncias.crear"),
    # path('editar/<int:id>',  views.logout, name="denuncias.editar"),
    # path('eliminar/<int:id>',  views.logout, name="denuncias.eliminar"),
]
