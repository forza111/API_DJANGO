from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Polls,Question


def index(request):
    latest_polls_list = Polls.objects.filter(end_date__gte=timezone.now()).order_by('-start_date')[:20]
    context = {'latest_polls_list':latest_polls_list}
    return render(request, 'polls/index.html', context)

def questions(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, {'question' : question})

# Create your views here.
