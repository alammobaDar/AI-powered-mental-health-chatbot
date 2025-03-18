from .views import chat, chatpage_view
from django.urls import path

app_name = "chat"
urlpatterns = [
    path("chat/",  chat, name="chat"),
    path("chatpage/", chatpage_view, name="chatpage")  
]