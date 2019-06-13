from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views.generic import View
from .models import *
from comments.forms import CommentForm
from comments.models import Comment
from django.http import HttpResponse
# Create your views here.
class IndexView(View):
    """
    文章列表页视图类
    """
    def get(self,req):
        """
        重写get请求
        :param req:
        :return:
        """
        articles=Article.objects.all()
        return render(req,"blog/index.html",locals())

class SingleView(View):
    """
    文章详情页视图
    """
    def get(self,req,id):
        """

        :param req:
        :param id:
        :return:
        """
        article=get_object_or_404(Article,pk=id)
        #向详情页面传递一个 评论表单
        cf=CommentForm()
        return render(req,"blog/single.html",locals())

    def post(self,req,id):
        name=req.POST.get("name")
        url = req.POST.get("url")
        email = req.POST.get("email")
        content = req.POST.get("content")

        comment=Comment()
        comment.name=name
        comment.url = url
        comment.email = email
        comment.content=content
        comment.article = get_object_or_404(Article,pk=id)

        comment.save()
        return redirect(reverse("blog:single",args=(id,)))