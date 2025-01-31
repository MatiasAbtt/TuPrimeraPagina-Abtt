from django.urls import path
from .views import send_message, inbox, sent_messages

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
    path('sent/', sent_messages, name='sent_messages'),
]