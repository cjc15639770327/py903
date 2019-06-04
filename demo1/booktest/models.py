from django.db import models
class BookInfo(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateField()

class HeroInfo(models.Model):
    name=models.CharField(max_length=20)
    gender=models.BooleanField(default=True)
    content=models.CharField(max_length=100)

    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
# Create your models here.
