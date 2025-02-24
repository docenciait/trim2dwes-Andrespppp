from . import views
from django.urls import path, include 

# Create your views here.
#  usuarios/urls.py: 
# i. /registro/: Vista registro. 
# ii. /login/: Vista iniciar_sesion. 
# iii. /logout/: Vista cerrar_sesion. 

#
urlpatterns = [
    path('', views.index, name='usuarios.index'),
    path('signup', views.signup, name="usuarios.signup"),
    path('login', views.login, name="usuarios.login"),
    path('logout', views.logout, name="usuarios.logout"),
]
