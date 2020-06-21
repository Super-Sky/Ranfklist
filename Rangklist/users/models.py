
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    """
    用户
    """
    name = models.CharField(max_length=30,null=False,verbose_name="客户端id")
    fraction = models.IntegerField(null=True,verbose_name="分数")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name
