from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    """
    标签表：与文章表存在多对多
    title：标签标题
    """
    title=models.CharField(max_length=20,)

    def __str__(self):
        return self.title

class Category(models.Model):
    """
    分类表：与文章表存在一对多
    title：分类标题
    """
    title=models.CharField(max_length=30,)

    def __str__(self):
        return self.title

class Article(models.Model):
    """
    文章表：与标签表多对多 与分类表多对一
    """
    title=models.CharField(max_length=20)
    body=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    create_time=models.DateTimeField(auto_now=True)
    tags=models.ManyToManyField(Tag)
    update_time=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.title


