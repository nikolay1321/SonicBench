from django.urls import path

from .views import(
    BrandListView,
    BrandDetailView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
)

app_name = "brands"

urlpatterns = [
    path(
        "",
        BrandListView.as_view(),
        name="brand_list",
    ),

    path(
        "add/",
        BrandCreateView.as_view(),
        name="brand_add",
    ),

    path(
        "<int:pk>/",
        BrandDetailView.as_view(),
        name="brand_detail",
    ),

    path(
        "<int:pk>/edit/",
        BrandUpdateView.as_view(),
        name="brand_edit",
    ),

    path(
        "<int:pk>/delete/",
        BrandDeleteView.as_view(),
        name="brand_delete",
    ),
]