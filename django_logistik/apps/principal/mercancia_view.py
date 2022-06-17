from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import MercanciaForm
from .models import Mercancia


class MercanciaUpdate(UpdateView):
    model = Mercancia
    form_class = MercanciaForm
    template_name = 'principal/modificar_mercancia.html'
    success_url = reverse_lazy('home')