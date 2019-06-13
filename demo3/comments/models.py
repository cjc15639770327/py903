from django.db import models
from blog.models import Article

# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=30,verbose_name="名字")
    create_time=models.DateTimeField(auto_now=True)
    content=models.CharField(max_length=500,verbose_name="正文")
    email=models.EmailField(blank=True,null=True,verbose_name="邮箱")
    url=models.URLField(blank=True,null=True,verbose_name="个人主页")
    article=models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.name