from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import ProductoList, ProductoDetalle, CategoriaList, SubCategoriaList, CategoríaDetalle, SubCategoriaList, SubCategoriaAdd, ProductoViewSet

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
    path('v1/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(), name='sc_add')
]

urlpatterns += router.urls
