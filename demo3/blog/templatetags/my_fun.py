"""
扩展自定义标签
"""

from ..models import Article,Category,Tag
from django.template import Library

register=Library()

@register.simple_tag
def getlatestarticles(num=3):
    """
    得到最新的文章
    :return:
    """
    return Article.objects.all().order_by("-create_time")[:num]

@register.simple_tag
def getarchives():
    return Article.objects.dates("create_time","month")

@register.simple_tag
def getcategorys():
    return Category.objects.all()


@register.simple_tag
def gettags():
    return Tag.objects.all()