from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Polls,Question,Choice



def index(request):
    latest_polls_list = Polls.objects.filter(end_date__gte=timezone.now()).order_by('-start_date')[:20]
    context = {'latest_polls_list':latest_polls_list}
    return render(request, 'polls/index.html', context)


def detail(request, polls_id):
    polls = get_object_or_404(Polls, pk=polls_id)
    return render(request, 'polls/detail.html', {'polls': polls})


def detail_question(request, polls_id, question_id):
    polls = get_object_or_404(Polls, pk=polls_id)
    question = get_object_or_404(Question, polls = polls, pk = question_id)
    return render(request, 'polls/detail_question.html', {'polls': polls, 'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,
                                                     'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))