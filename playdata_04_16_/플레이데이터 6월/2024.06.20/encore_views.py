from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

########
import requests 
api_url = "http://ip:port/predict/"
########


def index(request):
    page = request.GET.get('page', '1')

    question_object = Question.objects.order_by('-create_date')
    
    paginator = Paginator(question_object, 10)
    page_obj = paginator.get_page(page)

    return render(request, 'encore/question_list.html',
            {'question_list' : page_obj}      )

@login_required(login_url='common:login')
def detail(request, question_id):
    q  = get_object_or_404(Question, pk=question_id)
    return render(request,'encore/question_detail.html', {'question' : q})

@login_required(login_url='common:login')
def answer_create(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            #rt = requests.post(api_url, data={'message' : answer.content}).json()
            #print(rt)
            # if rt['proba'] > 0.5:
            #     answer.emotion = "&#x1F604"
            # else:
            #     answer.emotion = "&#x1F622"
            answer.emotion = "&#x1F604"
            answer.question = q
            answer.save()
            return redirect('encore:detail', question_id=q.id)
    else:
        form = AnswerForm()
    context = {'question' : q, 'form' : form}
    return render(request, 'encore/question_detail.html', context) 
    
@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quthor = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('encore:index')
    else:
        print("get 방식이여~~~~")
        form = QuestionForm()
    
    return render(request, 'encore/question_form.html', {'form' : form })

@login_required(login_url='common:login')
def question_modify(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    if request.user != question.quthor:
        messages.error(request,"수정권한 없음 ")
        return redirect("encore:detail", question_id = question.id)
    else:
        if request.method == "POST":
            # 다음번부턴 post
            form = QuestionForm(request.POST,instance=question)
            if form.is_valid():
                form.save(commit=False)
                question.quthor = request.user
                question.modify_date = timezone.now()
                question.save()
                return redirect("encore:detail",question_id = question.id)
            # pass
        else: #처음 글쓸땐 무주건 get
            form = QuestionForm(instance=question)
        context = {'form' : form}
        return render(request, 'encore/question_form.html',context)
    
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    if request.user != question.quthor:
        messages.error(request,"삭제권한없음")
        return redirect("encore:detail",question_id = question.id)
    else:
        question.delete()
    return redirect('encore:index')
