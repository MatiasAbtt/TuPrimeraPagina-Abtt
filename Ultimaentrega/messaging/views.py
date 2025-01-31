from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from django.contrib import messages

@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_username = request.POST.get('receiver')
        content = request.POST.get('content')

        try:
            receiver = User.objects.get(username=receiver_username)
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            messages.success(request, 'Mensaje enviado con éxito.')
            return redirect('inbox')
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe.')
            return redirect('send_message')

    users = User.objects.exclude(username=request.user.username)
    return render(request, 'messaging/send_message.html', {'users': users})

@login_required
def inbox(request):
    messages_received = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'messages_received': messages_received})

@login_required
def sent_messages(request):
    messages_sent = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messaging/sent_messages.html', {'messages_sent': messages_sent})

