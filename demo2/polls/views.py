from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import Question,Choice
# Create your views here.

class IndexView(View):

    def get(self,req):
        questions=Question.objects.all()
        return render(req,'polls/index.html',locals())

class DetailView(View):
    def get(self,req,id):
        question=Question.objects.get(pk=id)
        return render(req,'polls/detail.html',locals())

    def post(self,req,id):
        c_id=req.POST.get("info")
        choice=Choice.objects.get(pk=c_id)
        choice.vites +=1
        choice.save()
        return redirect(reverse("polls:result",args=(id,)))

class ResultView(View):
    def get(self,req,id):
        question = Question.objects.get(pk=id)
        return render(req,"polls/result.html",locals())