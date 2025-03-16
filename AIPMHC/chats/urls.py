from .views import chat
from django.urls import path

urlpatterns = [
    path("chat/",  chat, name="chat")
]