from django.urls import path

from .views import(
    SpeakerListView,
    SpeakerCreateView,
    SpeakerUpdateView,
    SpeakerDeleteView,
    SpeakerDetailView,
)

app_name = "speakers"

urlpatterns = [
    path(
        "",
        SpeakerListView.as_view(),
        name="speaker_list",
    ),

    path(
        "add/",
        SpeakerCreateView.as_view(),
        name="speaker_add",
    ),

    path(
        "<int:pk>/",
        SpeakerDetailView.as_view(),
        name="speaker_detail",
    ),

    path(
        "<int:pk>/edit/",
        SpeakerUpdateView.as_view(),
        name="speaker_edit",
    ),

    path(
        "<int:pk>/delete/",
        SpeakerDeleteView.as_view(),
        name="speaker_delete",
    ),
]