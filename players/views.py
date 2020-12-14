from django.shortcuts import render
from django.utils import timezone
from .models import Player
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PlayerForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)


class PlayerListView(ListView):
    model = Player

    def get_queryset(self):
        return Player.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PlayerDetailView(DetailView):
    model = Player

class CreatePlayerView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/player_detail.html'

    form_class = PlayerForm
    model = Player

class UpdatePlayerView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/player_detail.html'

    form_class = PlayerForm
    model = Player

class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = reverse_lazy('player_list')