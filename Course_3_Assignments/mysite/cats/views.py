from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat, Breed
from django.views import generic

# Create your views here.

#Breed CRUD Views

#Breed Create View
class BreedCreate(CreateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy('cats:all')

#Breed Reed View (List View)
class BreedList(LoginRequiredMixin, generic.ListView):
    model = Breed
    """def get(self, request):
        breed_list = Breed.objects.all()
        breed_count = Breed.objects.all().count()
        cnx = { "breeds": breed_list, "breed_count": breed_count}
        return render(request, "cats/breed_list.html", cnx)"""

#Breed Update View
class BreedUpdate(UpdateView, LoginRequiredMixin):
    model= Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

#Breed Delete View
class BreedDelete(DeleteView, LoginRequiredMixin):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

#Cats CRUD Views

#Cat Create View
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

#Cat Reed Vie (List View)
class CatList(LoginRequiredMixin, generic.ListView):
    model = Cat
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['breed_count'] = Breed.objects.all().count()
            return context
    '''def get(self, request):
        cat_list = Cat.objects.all()
        breed_count = Breed.objects.all().count()
        cnx = { "cat_list": cat_list, "breed_count": breed_count}
        return render(request, "cats/cat_list.html", cnx)'''

#Cats Update View
class CatUpdate(UpdateView, LoginRequiredMixin):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

#Cats Delete View
class CatDelete(DeleteView, LoginRequiredMixin):
     model = Cat
     fields = '__all__'
     success_url = reverse_lazy('cats:all')

