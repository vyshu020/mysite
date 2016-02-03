
from django.shortcuts import render, get_object_or_404
from models import Question, Choice
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.views import generic

#generic View
class IndexView(generic.ListView):
    context_object_name = 'my_latest_questions_inside_template'
    template_name = 'polls/index.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
"""
def index(request):
    my_latest_questions = Question.objects.order_by('pub_date')[:5]
    context = {
        'my_latest_questions_inside_template': my_latest_questions,
    }
    return render(request,'polls/index.html',context)
"""
def about_us(request):
    return HttpResponse("I have created this site. My name is Vyshnavi.")

class DetailView(generic.DetailView):
    model=Question
    template_name = 'polls/details.html'
"""
def detail(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    context ={'question':question}
    return render(request,'polls/details.html',context)
"""

class ResultsView(generic.DetailView):
    model=Question
    template_name = 'polls/results.html'
"""
def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""
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