
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def about_us(request):
    return HttpResponse("I have created this site. My name is Vyshnavi.")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." %question_id)

def results(request, question_id):
    response="You are looking at the results of question %s."
    return HttpResponse(response % qusetion_id)

def vote(request, question_id):
    return HttpResponse("you are voting on question %s."%question_id)