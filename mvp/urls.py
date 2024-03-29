"""mvp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from pedido.api.viewsets import PedidoViewSet
from pecas.api.viewsets import PecasViewSet
from cliente.api.viewsets import ClienteViewSet
from enderecoEntrega.api.viewsets import EnderecoEntregaViewSet
from anunciante.api.viewsets import AnucianteViewSet

# Rotas das APIs
router = routers.DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'pecas', PecasViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'enderecoEntrega', EnderecoEntregaViewSet)
router.register(r'anunciante', AnucianteViewSet)

# Rota dos anunciante
#router = routers.DefaultRouter()
#router.register(r'anunciante/', )



#Rotas dos administradores
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('anunciante/', admin.site.urls),
]
