from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .apiviews import *

from rest_framework_swagger.views import get_swagger_view 
from rest_framework.documentation import include_docs_urls

router = DefaultRouter() 
#router.register('v2/productos/', ProductoViewSet, name='productos')
router.register('v2/productos', ProductoViewSet, basename='productos')

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list' ),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle' ),
    path('v1/categorias/', CategoriaList.as_view(), name='categoria_save' ),
#    path('v1/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_save' ),
    path('v1/categorias/<int:pk>', CategoríaDetalle.as_view(), name='categoria_detalle' ),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name='sc_list'),
    path('v1/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(), name='sc_add'),
    path('v3/usuarios/', UserCreate.as_view(), name='user_create'),
    path('v4/login/', LoginView.as_view(), name='login'),
    path("v4/login-drf/", views.obtain_auth_token, name="login_drf"),
    #Tiene una parte publica y privada, para acceder a la privada necesito ser superuser
    path("swagger-docs", get_swagger_view(title='Documentación SWAGGER')),
    path('docs/', include_docs_urls(title='Documentación COREAPI'))
    
]

urlpatterns += router.urls
