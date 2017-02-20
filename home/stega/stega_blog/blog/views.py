#! -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from django.template import RequestContext
from blog.models import Post

class PostsListView(ListView):
    """ представление в виде списка """
    model = Post  # модель для представления

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['last_posts'] = self.model.objects.all().order_by('-id')[:5]
        return context

class PostDetailView(DetailView):
    """ детализированное представление модели """
    model = Post

def about_page(request):
    return render_to_response('blog/post_detail.html', RequestContext(request, {
        'post': Post.objects.get(pk=1)
    }))
