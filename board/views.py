# coding=utf8

from django.shortcuts import render
from .models import Message
from .forms import SubmitMessageForm


def message(request):
    if request.method == 'GET':
        return render(request, 'board/message.html')
    elif request.method == 'POST':
        form = SubmitMessageForm(request.POST)
        if form.is_valid():
            msg = Message(**form.cleaned_data)
            msg.save()
            return render(request, 'board/ok.html', locals())
        return render(request, 'board/message.html', locals())


def list_message(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        return render(request, 'board/list.html', locals())
