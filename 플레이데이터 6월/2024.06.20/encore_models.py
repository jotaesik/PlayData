from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    quthor = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True,blank=True) #처음 적으면 값이 다 없으므로 왜? 수정안하니깐
    # blank는 빈값들어오면 체크하지마!
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True,blank=True) 
    create_date = models.DateTimeField()
    emotion = models.TextField()

    def __str__(self):
        return self.content