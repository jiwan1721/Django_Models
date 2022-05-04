from django.urls import reverse
from django.shortcuts import render
from django.http import Http404
from sambho.models.test_models import *
from django.template.loader import get_template
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from sambho.models import *
from .models import *
# Create your views here.
def modelPractice(request):
    x = People.objects.filter(age = 45).count()
    y =[]
    for q in People.objects.all().order_by('age'):
        y.append(q.age)
    context = {
        'value':x
    }
    for p in PeopleAddress.objects.all().select_related('peoples')[0:10]:
        print(p.peoples.name)
    return HttpResponse(context)
def index(request):
    query_list = Quize.objects.all().order_by('published_date')[:5]
    template = loader.get_template('sambho/index.html')
    context = {
        'question_list': query_list
    }
    print("jhkfsjf",query_list)
    print(context)
    # print(query_list)
    # output= ','.join([q.question_area for q in query_list])
    #print(output)
    return HttpResponse(template.render(context,request))
def details(request,question_id):
    try:
        quiz = Quize.objects.get(pk=question_id)
    except:
        raise Http404("question doesnot exist")
    
    #shortcut for above program
    # quiz = get_object_or_404(Quize, pk = question_id)
    options = quiz.option_set.all()
    return render(request, 'sambho/detail.html',{
        'question': quiz,
        'options': options
        })

def results(request,question_id):
    quiz = get_object_or_404(Quize, pk = question_id)
    
    return render(request, 'sambho/result.html',{
        'quize':quiz
    })
def vote(request,question_id):
    quiz = get_object_or_404(Quize, pk = question_id)
    try:
        choosed_option = quiz.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Option.DoseNotExist):
        return render(request, 'sambho:detail.html', {
            'ques' : quiz,
            'error_message':"choice select garnu paryo razza.",
        })
    else:
        choosed_option.vote_count += 1
        choosed_option.save()
        
        return HttpResponseRedirect(reverse('sambho:results',args=(quiz.id,)))