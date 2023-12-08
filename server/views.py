from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
import os
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def waprfile(request):
    file_location = settings.BASE_DIR / 'staticfiles/files/image.jpg'

    try:    
        with open(file_location, 'rb') as f:
           file_data = f.read()

        # sending response 
        response = HttpResponse(file_data, content_type="image/jpeg")
        response['Content-Disposition'] = 'attachment; filename="image.jpg"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound(f'<h1>File not exist</h1>')
    
    except Exception as e:
        # log error here
        response = HttpResponseNotFound(f'<h1>{e}</h1>')

    return response

class ServerView():
    template_name = "template.html"

    def __init__(self, tn: str) -> None:
        self.template_name = tn

    def as_view(self):
        return TemplateView.as_view(template_name=self.template_name)

def index(request):
    return ServerView("server/index.html").as_view()(request, ip=get_client_ip(request))

def one(request):
    return ServerView("server/one.html").as_view()(request)

def two(request):
    return ServerView("server/two.html").as_view()(request)

@user_passes_test(lambda u: u.is_superuser)
def files_path(request, path: str):
    file_location = 'files/' + path

    if request.user.is_authenticated:
        if os.path.exists(os.path.abspath(os.path.dirname(__file__)).replace('server', 'static/' + file_location)):
            if path.endswith('.png') or path.endswith('.jpg') or path.endswith('.jpeg'):
                return ServerView("server/file_img.html").as_view()(request, filename=file_location)
            else:
                return ServerView("server/file_err.html").as_view()(request)
        else:
                return ServerView("server/file_err.html").as_view()(request)
    else:
        return ServerView("server/file_auth_err.html").as_view()(request)

@user_passes_test(lambda u: u.is_superuser) 
def files(request):
    return ServerView("server/files.html").as_view()(request)