from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings
import pickle, re
import numpy as np
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

loaded_model = None
tokenizer = None

def load_sentiment_model():
    global loaded_model, tokenizer
    loaded_model = load_model('/home/jotaesik/workspace/django/pybo/encore/best_model3.keras')
    with open('/home/jotaesik/workspace/django/pybo/encore/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
load_sentiment_model()
# Create your views here.
# 선언
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
            answer.create_date = timezone.now()
            text = answer.content
            print("시작")
            print(text)
            temp = sentiment_predict(text)
            print(temp)
            print("갑출력")
            if temp["result"]==1:
                answer.emotion = "&#x1F604"
            else:
                answer.emotion = "&#x1F622"
            print("끝")
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
            question.create_date = timezone.now()
            question.save()
            return redirect('encore:index')
    else:
        print("get 방식이여~~~~")
        form = QuestionForm()
    
    return render(request, 'encore/question_form.html', {'form' : form })

def sentiment_predict(new_sentence):
    # print("진입")
    # loaded_model = load_model('/home/jotaesik/workspace/django/pybo/encore/best_model3.keras')
    # with open('/home/jotaesik/workspace/django/pybo/encore/tokenizer.pickle', 'rb') as handle:
    #     tokenizer = pickle.load(handle)
    # print("model 읽기")
    
    # print("model읽기 성공")
    global loaded_model, tokenizer
    okt = Okt()
    stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
    max_len = 30
    print("불용어까지성공")
    # new_sentence = str(new_sentence)
    # print("1" + new_sentence)
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
    print("2" + new_sentence)
    new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    print(new_sentence)
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    print(new_sentence)
    encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    print(encoded)
    pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
    print("예측시작전")
    score = float(loaded_model.predict(pad_new)) # 예측
    print(score)
    if(score > 0.5):
        print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
        return {'result' : 1, 'proba': score}
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))
        return {'result' : 0, 'proba': score}
    

@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)


@api_view(["POST"])
def predict_model(request):
    # print(text)
    # text = request.data.get("text")
    text=request.content
    print("값은?")
    print(text)
    rt = sentiment_predict(text)
    print("값출력")
    print(rt) 
    return Response(rt)