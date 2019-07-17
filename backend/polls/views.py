from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World of Django")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5];
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(id = question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question Does not Exist')
    question = get_object_or_404(Question, pk = question_id)

    return render(request, 'polls/detail.html', {'question' : question})