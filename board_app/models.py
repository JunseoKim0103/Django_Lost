from django.db import models
from django.contrib.auth.models import User # 장고에서 제공하는 유저모델


# Create your models here.
class Board(models.Model):
    # author = models.ForeignKey(User, on_delete = models.CASCADE, max_length=10, null=False)
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=25, null=False)
    mainphoto = models.ImageField(upload_to = 'images/', blank=True, null=True)
    content = models.TextField(null=False)
    Lost_date = models.DateTimeField(auto_now_add=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(null = True, blank = True)
    #위치 : category형 
    #물품명 : category형


    def __str__(self):
        return self.subject # 관리자페이지에서 어떻게 보여질 것인가.
    
class Photo(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    mainphoto = models.ImageField(upload_to='images/', blank=True, null=True)