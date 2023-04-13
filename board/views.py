# board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Posting, Reply
from .forms import PostingForm, ReplyForm
from django.db.models import Count
from django.core.paginator import Paginator
import requests
from .utils.fish_list import get_fish_list


# 3102fefa-0819-4322-a697-abc0791c72d3 nookipedia key

@require_safe
def index(request):
    fish_list = get_fish_list()
    populars = Posting.objects.annotate(like_count=Count('like_users')).order_by('-like_count')[:5]
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    return render(request, 'board/index.html', {
        'user' : user,
        'populars' : populars,
        'fish_list' : fish_list,
    })

def fish_list_view(request):
    fish_list = get_fish_list()
    context = {"fish_list": fish_list}
    return render(request, "board/fishlist.html", context)

@require_safe
def posting_list(request):
    postings = Posting.objects.all().annotate(like_count=Count('like_users')).order_by('-like_count', '-updated_at')
    paginator = Paginator(postings, 10)
    page = request.GET.get('page')
    postings = paginator.get_page(page)
    context = {
        'postings': postings,
    }
    return render(request, 'board/posting_list.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.user = request.user
            posting.save()
            return redirect('board:detail', posting.pk)
    else : 
        form = PostingForm()
        return render(request, 'board/create.html', {
            'form' : form
        })
    
@require_http_methods(['GET', 'HEAD'])
def detail(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    # 댓글 index도 posting_detail 에서 진행
    replies = posting.reply_set.all()
    # 댓글 create도 posting_detail 에서 진행
    form = ReplyForm()
    is_like = posting.like_users.filter(pk=request.user.pk).exists()
    return render(request, 'board/detail.html', {
        'posting': posting,
        'replies': replies,
        'form': form,
        'is_like': is_like,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)

    if request.user != posting.user:
        return redirect('board:index')

    if request.method == 'POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save()
            return redirect('board:detail', posting.pk)
    else:
        form = PostingForm(instance=posting)
    return render(request, 'board/create.html', {
        'form': form,
    })


@login_required
@require_POST
def delete(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    
    if request.user != posting.user:
        return redirect('board:index')
        
    posting.delete()
    return redirect('board:index')


@login_required
@require_POST
def create_reply(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    form = ReplyForm(request.POST)

    if form.is_valid():
        reply = form.save(commit=False)  # 저장 멈춰! 
        reply.posting = posting  # 비어있는 컬럼 => FK
        reply.user = request.user
        reply.save()
    return redirect('board:detail', posting.pk)

@login_required
@require_POST
def delete_reply(request, posting_pk, reply_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)

    if request.user == reply.user:
        reply.delete()
        
    return redirect('board:detail', posting.pk)

@login_required
@require_POST
def like_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk = posting_pk)
    user = request.user
    if posting.like_users.filter(pk=user.pk).exists():
        posting.like_users.remove(user)
        # user in posting.like_users.all():
    else :
        posting.like_users.add(user)
    return redirect('board:detail', posting.pk)