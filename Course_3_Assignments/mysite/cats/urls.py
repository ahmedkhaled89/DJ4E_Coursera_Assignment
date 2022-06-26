from django.urls import path
from . import views
app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name='all' ),
    path('lookup/create', views.BreedCreate.as_view(), name="breed_create"),
    path('lookup', views.BreedList.as_view(), name= 'breed_list'),
    path('lookup/<int:pk>/update', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete', views.BreedDelete.as_view(), name='breed_delete'),
    path('main/create', views.CatCreate.as_view(), name = 'cat_create'),
    path('main/<int:pk>/update', views.CatUpdate.as_view(), name = 'cat_update'),
    
]
