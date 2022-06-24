from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
   path('autos/', include('autos.urls')),
   path('hello/', include('hello.urls')),
   path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    
]
