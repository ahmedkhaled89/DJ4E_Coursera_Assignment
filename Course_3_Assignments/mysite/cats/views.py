from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat, Breed
# Create your views here.

def testview(req):
    return HttpResponse("hello from cats app")

class CatList(LoginRequiredMixin, View):
    def get(self, request):
        cat_list = Cat.objects.all()
        breed_count = Breed.objects.all().count()
        cnx = { "cats": cat_list, "breed_count": breed_count}
        return render(request, "cats/cat_list.html", cnx)

class BreedCreate(CreateView):
    model = Breed
    fields = "__all__"
    success_url = reverse_lazy('cats:allcats')

