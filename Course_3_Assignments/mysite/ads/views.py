from tempfile import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from requests import request
from ads.forms import CreateForm
from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "ads/Ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad

class AdCreateView(LoginRequiredMixin, View):
    model = Ad
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    # List the fields to copy from the Ad model to the Ad form
    #fields = ['title', 'price', 'text', 'picture']
    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)
    
    def post(self, request, pk= None):
        form = CreateForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)

        


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']


class AdDeleteView(OwnerDeleteView):
    model = Ad
