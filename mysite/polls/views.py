
from django.http import HttpResponse
from models import Question, Choice
# Create your views here.

def index(request):
    my_latest_questions = Question.objects.order_by('pub_date')[:5]
    response = ','.join([q.question_text for q in my_latest_questions])
    return HttpResponse(response)

def about_us(request):
    return HttpResponse("I have created this site. My name is Vyshnavi.")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." %question_id)

def results(request, question_id):
    response="You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you are voting on question %s."%question_id)