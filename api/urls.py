from django.urls import path
from .apiviews import ProductoList, ProductoDetalle, CategoriaList, SubCategoriaList
 
urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list' ),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle' ),
    path('v1/categorias/', CategoriaList.as_view(), name='categoria_list' ),
    path('v1/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_list' ),
]