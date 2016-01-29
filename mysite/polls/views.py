
from django.shortcuts import render, get_object_or_404
from models import Question, Choice
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    my_latest_questions = Question.objects.order_by('pub_date')[:5]
    context = {
        'my_latest_questions_inside_template': my_latest_questions,
    }
    return render(request,'polls/index.html',context)

def about_us(request):
    return HttpResponse("I have created this site. My name is Vyshnavi.")

def detail(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    context ={'question':question}
    return render(request,'polls/details.html',context)

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html', {'question': question}),

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