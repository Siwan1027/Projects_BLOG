from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Posting, Reply
from .forms import PostingForm, ReplyForm

# Create your views here.

def index(request):
    return render(request, 'board/index.html')

def create(request):
    pass

def detail(request):
    pass

def update(request):
    pass

def delete(request):
    pass