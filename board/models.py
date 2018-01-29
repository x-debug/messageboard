# coding=utf8

from django.db import models


class Message(models.Model):
    """
        留言
    """

    name = models.CharField(verbose_name='姓名', max_length=20)

    email = models.EmailField(verbose_name='邮箱', max_length=50)

    address = models.CharField(verbose_name='聯系地址', max_length=100)

    content = models.TextField(verbose_name='留言內容')

    class Meta:
        verbose_name = '留言'

        verbose_name_plural = verbose_name

        ordering = ['-id']

    def __str__(self):
        return '{name}-{email}'.format(name=self.name, email=self.email)
