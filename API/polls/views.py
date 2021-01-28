from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Polls,Question,Choice



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_polls_list'

    def get_queryset(self):
        '''Return 20 actual polls, sorted by "start_date" column'''
        return Polls.objects.filter(end_date__gte=timezone.now()).order_by('-start_date')[:20]


class DetailView(generic.DetailView):
    model = Polls
    template_name = 'polls/detail.html'
    def get_queryset(self):
        '''Excludes any questions polls that aren't published yet'''
        return Polls.objects.filter(end_date__gte=timezone.now())


def detail_question(request, polls_id, question_id):
    polls = get_object_or_404(Polls, pk=polls_id)
    question = get_object_or_404(Question, polls = polls, pk = question_id)
    return render(request, 'polls/detail_question.html', {'polls': polls, 'question' : question})

def vote(request, polls_id, question_id):
    polls = get_object_or_404(Polls, pk=polls_id)
    question = get_object_or_404(Question, polls = polls, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,
                                                     'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))