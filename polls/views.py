from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import *
from .forms import *


def index(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    form = RawNewQuestion()
    context = {'object_list': None,
               'form': form,
               'latest_question_list': Question.objects.order_by('-pub_date')[:10]}
    if request.method == 'POST':
        form = RawNewQuestion(request.POST)
        if form.is_valid():
            Question.objects.create(**form.cleaned_data, author=user)
    queryset = Question.objects.all()
    context['object_list'] = reversed(queryset)
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = RawNewChoice()
    context = {'object_list': None,
               'form': form,
               'choices_list': question.choice_set.all(),
               'question': question}
    if request.method == 'POST':
        form = RawNewChoice(request.POST)
        if form.is_valid():
            Choice.objects.create(**form.cleaned_data, question=question)
    queryset = question.choice_set.all()
    context['object_list'] = reversed(queryset)
    return render(request, "polls/detail.html", context)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
