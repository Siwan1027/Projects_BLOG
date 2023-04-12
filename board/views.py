# board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Posting, Reply
from .forms import PostingForm, ReplyForm

@require_safe
def index(request):
    # postings = Posting.objects.order_by(Posting.like_user.count())
    return render(request, 'board/index.html')

@login_required
@require_POST
def create(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.user = request.user
            posting.save()
            return redirect(request, 'blog:detail', posting.pk)
    else : 
        form = PostingForm()
        return render(request, 'board:create', context ={
            'form' : form
        })
    
@require_safe
def detail(request,posting_pk):
    posting = get_object_or_404(Posting, pk = posting_pk)
    return render(request, 'blog:detail', context = {
        'posting' : posting
    })

@login_required
@require_POST
def update(request,posting_pk):
    pass
@login_required
@require_POST
def delete(request,posting_pk):
    pass