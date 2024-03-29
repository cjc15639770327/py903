from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views.generic import View
from .models import *
from comments.forms import CommentForm
from comments.models import Comment
from django.core.paginator import Paginator
import markdown
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMultiAlternatives
from demo3 import settings
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
        # latestarticles=articles.order_by("-create_time")[:1]

        # paginator=Paginator(articles,1)
        # print(paginator.count)
        # print(paginator.object_list)
        # print(paginator.num_psges)
        # print(paginator.page_range)
        # page=paginator.get_page(2)
        # print(page.object_list)
        # print(page.paginator)
        # print(page.number)
        # print(paginator is page.paginator)

        paginator = Paginator(articles, 1)
        pagenum=req.GET.get("page")
        pagenum=1 if pagenum==None else pagenum
        page=paginator.get_page(pagenum)
        page.path="/"
        return render(req,"blog/index.html",{"page":page})

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

        #1.获取markdown实例
        md=markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])

        #2.使用markdown实例渲染指定字段
        article.body=md.convert(article.body)
        #3.将md的目录对象赋予 article
        article.toc=md.toc



        #向详情页面传递一个 评论表单
        cf=CommentForm()
        articles=Article.objects.all()
        # latestarticles=articles.order_by("-create_time")[:1]
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

class ArchieveView(View):
    def get(self,req,year,month):
        articles=Article.objects.filter(create_time__year=year,create_time__month=month)
        paginator=Paginator(articles,1)
        pagenum=req.GET.get("page")
        pagenum= 1 if pagenum==None else pagenum
        page=paginator.get_page(pagenum)
        page.path="/archives/%s/%s"%(year,month)
        return render(req,"blog/index.html",{"page":page})

class CategoryView(View):
    def get(self,req,id):
        category=get_object_or_404(Category,pk=id)
        articles=category.article_set.all()
        paginator=Paginator(articles,1)
        pagenum=req.GET.get("page")
        pagenum= 1 if pagenum==None else pagenum
        page=paginator.get_page(pagenum)
        page.path="/category/%s/"%(id,)
        return render(req, "blog/index.html", locals())

class TagView(View):
    def get(self,req,id):
        tag=get_object_or_404(Tag,pk=id)
        articles=tag.article_set.all()
        page=getpageinfo(req,articles,1,"/tags/%s/"%(id,))
        # paginator=Paginator(articles,1)
        # pagenum=req.GET.get("page")
        # pagenum= 1 if pagenum==None else pagenum
        # page=paginator.get_page(pagenum)
        # page.path="/tags/%s/"%(id,)
        return render(req, "blog/index.html", locals())


class ContactView(View):
    def get(self,req):
        return render(req,"blog/contact.html")


    def post(self,req):
        email=req.POST.get("email")
        message=req.POST.get("message")

        info=MessageInfo()
        info.email=email
        info.info=message
        info.save()


        return HttpResponse("提交成功")

class SendMailView(View):
    def get(self,req):
        "发送邮件"

        try:
            mail=EmailMultiAlternatives(subject="测试邮件html格式",body="<h1><a href='http://www.baidu.com'>百度</a></h1>",from_email=settings.DEFAULT_FROM_EMAIL,to=["15639770327@163.com"])
            mail.content_subtype="html"
            mail.send()
            # send_mail("测试邮件", "<h1><a herf='http://www.baidu.com'>百度</a></h1>", settings.DEFAULT_FROM_EMAIL, ["15639770327@163.com"])
            return HttpResponse("发送成功")
        except:
            return HttpResponse("发送失败")