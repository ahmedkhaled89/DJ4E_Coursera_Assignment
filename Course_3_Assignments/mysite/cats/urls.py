from django.urls import path
from . import views
app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name='allcats' )
]