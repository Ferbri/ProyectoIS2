from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404,render

def index(request):
   latest_question_list = Question.objects.order_by('-pub_date')[:5]
   context = {'latest_question_list': latest_question_list}
   return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You are looking at the results of QUESTION %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on QUESTION %s." % question_id)