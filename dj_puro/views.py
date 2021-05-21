from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from dj_puro.models import Categoria

def categoria_list(request):
    MAX_OBJECTS = 20
    categorias = Categoria.objects.all()[:MAX_OBJECTS]
    data = {"result": list(categorias.values('descripcion', 'activo'))}
    return JsonResponse(data)

def categoria_detalle(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    data = {"result": 
        {
            "descripcion": categoria.descripcion,
            "activo": categoria.activo
        }
    }
    return JsonResponse(data)