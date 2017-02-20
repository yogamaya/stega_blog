#! -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()  # функция автоматического обнаружения файлов admin.py в наших приложениях

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^blog/', include('blog.urls')),
    url(r'.*?', include('blog.urls')),
]
