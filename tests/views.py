# coding: utf-8

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import six


def execute_sql(request):
    list(User.objects.all())
    return HttpResponse()


def non_ascii_context(request):
    class NonAsciiRepr(object):
        def __repr__(self):
            return 'nôt åscíì' if six.PY3 else 'nôt åscíì'.encode('utf-8')
    return render(request, 'basic.html', {'title': NonAsciiRepr()})


def regular_view(request, title):
    return render(request, 'basic.html', {'title': title})


def resolving_view(request, arg1, arg2):
    # see test_url_resolving in tests.py
    return HttpResponse()


def set_session(request):
    request.session['où'] = 'où'
    if not six.PY3:
        request.session['là'.encode('utf-8')] = 'là'.encode('utf-8')
    return render(request, 'basic.html')
