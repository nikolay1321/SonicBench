from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from .models import Speaker
from .forms import SpeakerForm, SpeakerEditForm

# Create your views here.

def home(request):
    latest_speakers = (
        Speaker.objects.select_related("brand").order_by("-created_at")[:3]
    )

    return render(request, "home.html", {"latest_speakers": latest_speakers,},)

class SpeakerListView(ListView):
    model = Speaker
    template_name = "speakers/speaker_list.html"
    context_object_name = "speakers"
    paginate_by = 6

    def get_queryset(self):
        queryset = Speaker.objects.select_related("brand")

        search_query = self.request.GET.get("q", "").strip()
        sort_by = self.request.GET.get("sort", "newest")

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(brand_name__icontains=search_query)
            )

        sorting_options = {
            "newest": "-created_at",
            "price_low": "price",
            "price_high": "-price",
            "name": "name",
        }

        return queryset.order_by(
            sorting_options.get(sort_by, "-created_at"),
            "pk",
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_query"] = self.request.GET.get("q", "").strip()

        context["current_sort"] = self.request.GET.get("sort", "newest")

        return context

class SpeakerDetailView(DetailView):
    model = Speaker
    template_name = "speakers/speaker_detail.html"
    context_object_name = "speaker"

class SpeakerCreateView(CreateView):
    model = Speaker
    form_class = SpeakerForm
    template_name = "speakers/speaker_form.html"

    def get_success_url(self):
        return reverse("speakers:speaker_detail", kwargs={"pk": self.object.pk},)

class SpeakerUpdateView(UpdateView):
    model = Speaker
    form_class = SpeakerEditForm
    template_name = "speakers/speaker_form.html"

    def get_success_url(self):
        return reverse("speakers:speaker_detail", kwargs={"pk": self.object.pk},)


class SpeakerDeleteView(DeleteView):
    model = Speaker
    template_name = "speakers/speaker_confirm_delete.html"
    success_url = reverse_lazy("speakers:speaker_list")