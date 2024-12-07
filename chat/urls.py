# chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('private/', views.private_chat_list_view, name='private_chat_list'),
    path('private/<int:user_id>/send/', views.send_private_message_view, name='send_private_message'),
]
