# chat/urls.py
from django.urls import path

from chatroom.views import *

app_name = "chatroom"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<str:room_name>/", RoomsView.as_view(), name="room"),
    # path("upload/<str:room_name>/, upload_file, name="upload_file"),
]
