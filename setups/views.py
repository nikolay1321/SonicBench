from django.db import models
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, CreateView, DetailView, UpdateView, DeleteView)


from .forms import RoomForm, ListeningSetupForm
from .models import Room, ListeningSetup

# Create your views here.

class RoomListView(ListView):
    model = Room
    template_name = "setups/room_list.html"
    context_object_name = "rooms"

class RoomDetailView(DetailView):
    model = Room
    template_name = "setups/room_detail.html"
    context_object_name = "room"

class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "setups/room_form.html"

    def get_success_url(self):
        return reverse("setups:room_detail", kwargs={"pk": self.object.pk},)

class ListeningSetupListView(ListView):
    model = ListeningSetup
    template_name = "setups/setup_list.html"
    context_object_name = "setups"

    def get_queryset(self):
        return ListeningSetup.objects.select_related("room").prefetch_related("speakers")

class ListeningSetupDetailView(DetailView):
    model = ListeningSetup
    template_name = "setups/setup_detail.html"
    context_object_name = "setup"

    def get_queryset(self):
        return ListeningSetup.objects.select_related("room").prefetch_related("speakers__brand")

class ListeningSetupCreateView(CreateView):
    model = ListeningSetup
    form_class = ListeningSetupForm
    template_name = "setups/setup_form.html"

    def get_success_url(self):
        return reverse("setups:setup_detail", kwargs={"pk": self.object.pk},)

class ListeningSetupUpdateView(UpdateView):
    model = ListeningSetup
    form_class = ListeningSetupForm
    template_name = "setups/setup_form.html"

    def get_success_url(self):
        return reverse("setups:setup_detail", kwargs={"pk": self.object.pk},)

class ListeningSetupDeleteView(DeleteView):
    model = ListeningSetup
    template_name = "setups/setup_confirm_delete.html"
    success_url = reverse_lazy("setups:setup_list")