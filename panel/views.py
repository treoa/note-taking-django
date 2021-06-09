from django.db.models import query
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import Q, TextField
from django.db.models.functions import Lower
from django.db.models.query import QuerySet

from .models import Content
from .forms import BaseViewForm, UpdateViewForm

# Create your views here.
TextField.register_lookup(Lower, 'lower')


class ContentAsList (LoginRequiredMixin, ListView):
    model = Content
    template_name = 'panel/main.html'
    context_object_name = 'content'
    ordering = ['date_created']
    paginate_by = 50

    def get_queryset(self):
        my_query=self.request.GET.get('search', '')
        queries = Content.objects.filter(Q(content__lower__contains=query)).order_by('date_created')
        return queries


class CreateContent(LoginRequiredMixin, CreateView):
    model = Content
    form_class = BaseViewForm
    template_name = 'panel/content_create.html'
    success_url = '/'

    def form_ok (self, form):
        form.instance.author = self.request.user
        return super().form_ok(form)

    
class UpdateContent(LoginRequiredMixin, UpdateView):
    model = Content
    form_class = UpdateViewForm
    template_name = 'panel/content_update.html'

    def form_ok(self, form):
        form.instance.author = self.request.user
        return super().form_ok(form)


class DeleteContent(LoginRequiredMixin, DeleteView):
    model = Content
    success_url = '/'
    template_name = 'panel/content_delete.html'


def csrf_failure(request, reason=""):
    current_page = request.path
    try:
        if '/content/new' in current_page:
            return CreateContent.as_view()(request)
        elif '/update' in current_page:
            return UpdateContent.as_view()(request)
        elif '/delete' in current_page:
            return DeleteContent.as_view()(request)
        else:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')


class DetailedContent(LoginRequiredMixin, DetailView):
    model = Content
