from django.urls import path
from . import views
app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name='all' ),
    path('create', views.BreedCreate.as_view(), name="breed_create")
]