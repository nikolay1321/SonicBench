from django.urls import path
from .views import (RoomListView, RoomDetailView, RoomCreateView, ListeningSetupCreateView, ListeningSetupUpdateView, ListeningSetupDeleteView, ListeningSetupDetailView, ListeningSetupListView)

app_name = "setups"

urlpatterns = [
    path(
        "rooms/",
        RoomListView.as_view(),
        name="room_list",
    ),

    path(
        "rooms/add/",
        RoomCreateView.as_view(),
        name="room_add",
    ),

    path(
        "rooms/<int:pk>/",
        RoomDetailView.as_view(),
        name="room_detail",
    ),

    path(
        "setups/",
        ListeningSetupListView.as_view(),
        name="setup_list",
    ),

    path(
        "setups/add/",
        ListeningSetupCreateView.as_view(),
        name="setup_add",
    ),

    path(
        "setups/<int:pk>/",
        ListeningSetupDetailView.as_view(),
        name="setup_detail",
    ),

    path(
        "setups/<int:pk>/edit/",
        ListeningSetupUpdateView.as_view(),
        name="setup_edit",
    ),

    path(
        "setups/<int:pk>/delete/",
        ListeningSetupDeleteView.as_view(),
        name="setup_delete",
    ),
]