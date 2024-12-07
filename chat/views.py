# chat/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import PrivateMessage
from django.contrib.auth.decorators import login_required

@login_required
def private_chat_list_view(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user from the list
    return render(request, 'chat/private_chat_list.html', {'users': users})


@login_required
def send_private_message_view(request, user_id):
    recipient = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            PrivateMessage.objects.create(sender=request.user, recipient=recipient, message=message_content)
            # Redirect back to the current page (send_private_message.html)
            return redirect('chat:send_private_message', user_id=user_id)

    # Fetch existing messages
    messages = PrivateMessage.objects.filter(sender=request.user, recipient=recipient) | PrivateMessage.objects.filter(
        sender=recipient, recipient=request.user)
    messages = messages.order_by('timestamp')  # Order messages by timestamp

    return render(request, 'chat/send_private_message.html', {'recipient': recipient, 'messages': messages})
