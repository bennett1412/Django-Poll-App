from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
#from django.views import generic
from .forms import QuestionForm,ChoiceForm
from .models import Choice, Question


def IndexView(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {
        'latest_question_list' : latest_question_list
    } 
    return render(request,'polls/index.html', context)  


def DetailView(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    context = {
        'question' : question
    }
    return render(request,"polls/details.html",context)

def ResultsView(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question' : question
    } 
    return render(request, "polls/results.html",context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def CreatePollView(request):
    if request.method == "POST":
        qform = QuestionForm(request.POST, instance = Question())
        cform = [ChoiceForm(request.POST,prefix = str(x),instance = Choice()) for x in range(0,3)]
        if qform.is_valid() and all ([cf.is_valid] for cf in cform):
            new_poll = qform.save()
            new_poll.save()
            for cf in cform:
                new_choice = cf.save(commit = False)
                new_choice.question = new_poll
                new_choice.save()
        
            return HttpResponseRedirect(reverse('polls:index'))
 
    else:
        qform = QuestionForm(instance = Question())
        cform = [ChoiceForm(prefix = str(x),instance = Choice()) for x in range(0,3)]
        return render(request,'polls/create.html',{'question_form' : qform, 'choice_form' : cform})            
