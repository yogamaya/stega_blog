#! -*- coding: utf-8 -*-

from django.db import models
from uuslug import slugify # Это библиотека для преобразования заголовков в ссылки django-uuslug


class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    #teaser = models.TextField(max_length=5000) #текст первого абзаца поста
    content = models.TextField(max_length=100000) # текст поста
    #slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True # Поле для записи ссылки

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        #return "/blog/{}/".format(self.id)
        return "/{}/".format(self.id)


class About(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    #teaser = models.TextField(max_length=5000) #текст первого абзаца поста
    content = models.TextField(max_length=100000) # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/{}/".format("about")
