from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import *
from .forms import *


def index(request):
    form = RawNewRecord
    context = {'object_list': None,
               'form': form,
               'records_list': Record.objects.order_by('category')}
    if request.method == 'POST':
        form = RawNewRecord(request.POST)
        if form.is_valid():
            Record.objects.create(**form.cleaned_data)
    queryset = Record.objects.all()
    context['object_list'] = reversed(queryset)
    return render(request, "records/index.html", context)


def detail(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    form = RawNewBreak()
    context = {'object_list': None,
               'form': form,
               'breaks_list': record.history.order_by('-current_break'),
               'record': record}
    if request.method == 'POST':
        form = RawNewBreak(request.POST)
        if form.is_valid():
            if form.cleaned_data['breaker_login'] == '':
                form.cleaned_data.pop('breaker_login')
                Break.objects.create(**form.cleaned_data, breaker_login=None, record=record)
            else:
                Break.objects.create(**form.cleaned_data, record=record)
    queryset = record.history.all()
    context['object_list'] = reversed(queryset)
    return render(request, "records/detail.html", context)
