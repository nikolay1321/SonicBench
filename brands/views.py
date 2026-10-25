from django.shortcuts import render
from django.db.models.deletion import ProtectedError
from django.urls import reverse, reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import BrandForm
from .models import Brand

# Create your views here.

class BrandListView(ListView):
    model = Brand
    template_name = "brands/brand_list.html"
    context_object_name = "brands"

class BrandDetailView(DetailView):
    model = Brand
    template_name = "brands/brand_detail.html"
    context_object_name = "brand"

class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = "brands/brand_form.html"

    def get_success_url(self):
        return reverse(
            "brands:brand_detail",
            kwargs={"pk": self.object.pk},
        )

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = "brands/brand_form.html"

    def get_success_url(self):
        return reverse(
            "brands:brand_detail",
            kwargs={"pk": self.object.pk},
        )

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = "brands/brand_confirm_delete.html"
    success_url = reverse_lazy("brands:brand_list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)

        except ProtectedError:
            form.add_error(
                None,
                "This brand cannot be deleted because it has speakers associated with it."
            )

            return self.form_invalid(form)