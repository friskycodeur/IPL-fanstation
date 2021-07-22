from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Player
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PlayerForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)


class PlayerListView(ListView):
    model = Player
    template_name='players/player_list.html'


class PlayerDetailView(DetailView):
    model = Player
    template_name='players/player_detail.html'

class CreatePlayerView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name='players/player_form.html'
    redirect_field_name = 'players/player_detail.html'

    form_class = PlayerForm
    model = Player

class UpdatePlayerView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'players/player_detail.html'

    form_class = PlayerForm
    model = Player

class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = reverse_lazy('player_list')

@login_required
def player_publish(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.publish()
    return redirect('player_detail', pk=pk)