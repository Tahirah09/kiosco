from django.urls import path
from apps.despensa.views import ProductoUpdateView, ProductoCreateView, ProductoDeleteView, ProductoListView, CategoriaUpdateView, CategoriaCreateView, CategoriaDeleteView, CategoriaListView



app_name = 'despensa'


urlpatterns = [
    path('nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('lista/', ProductoListView.as_view(), name='producto_list'),
    path('editar/', ProductoUpdateView.as_view(), name=' producto_update'),
    path('eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('nuevo/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('lista/', CategoriaListView.as_view(), name='categoria_list'),
    path('editar/', CategoriaUpdateView.as_view(), name=' categoria_update'),
    path('eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),

]