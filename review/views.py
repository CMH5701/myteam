from django.shortcuts import render

# Create your views here.

from email.policy import default
from django.shortcuts import render, redirect, get_object_or_404
from review.forms import ReviewForm, r_commentForm
from django.utils import timezone
from review.models import Review, r_comment
from main.models import Hashtag
from django.http import request
from django.core.paginator import Paginator # 페이징

# Create your views here.

#리뷰 작성
def r_write(request, review = None) :
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance = review)

        if form.is_valid():
            review = form.save(commit=False)
            review.r_date = timezone.now() 
            review.save()
            form.save_m2m()
                
            return redirect('r_list')
    else:
        form = ReviewForm(instance = review)
        return render(request, 'r_write.html', {'form':form })

#리뷰 목록
def r_list(request):
    reviews = Review.objects
    r_sort = request.GET.get('sort', '') 
    if r_sort == 'r_clicks':
        reviews = Review.objects.all().order_by('-r_clicks','-r_date')
    else:
        reviews = Review.objects.all().order_by('-r_date')
    #default_r_clikes = blogs.r_clikes
    # blogs.r_clikes = default_r_clikes +1
    return render(request, 'r_list.html', {'reviews':reviews, 'sort':r_sort})


def r_page(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    r_blogs = Review.objects.order_by('-r_date')

    # 페이징처리
    paginator = Paginator(r_blogs, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'r_blogs': page_obj}
    return render(request, 'community/community.html', context)

#리뷰 글 상세페이지
def r_detail(request, id):
    review = get_object_or_404(Review, id=id)

    if request.method == "POST" :
        form = r_commentForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit = False)
            comment.r_id = review
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('r_detail', id)
            
    else :
        form = r_commentForm()
        return render(request, 'r_detail.html', {'review':review, 'form':form})

#리뷰 수정
def r_edit(request, id):
    review = get_object_or_404(Review, id=id)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('r_list')
    else:
        form = ReviewForm(instance=review)
        return render(request, 'r_edit.html', {'form':form})

#리뷰 삭제
def r_delete(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    return redirect('r_list')

#좋아요 
def r_likes(request, r_id):
    like_b = get_object_or_404(Review, id=r_id)
    if request.name in like_b.r_like.all():
        like_b.r_like.remove(request.name)
        like_b.r_likes -= 1
        like_b.save()
    else:
        like_b.r_like.add(request.name)
        like_b.r_likes += 1
        like_b.save()
    return redirect('/r_detail/' + str(r_id))

#추천수 
def r_clip(request, r_id):
    like_b = get_object_or_404(Review, id=r_id)
    if request.name in like_b.r_clip.all():
        like_b.r_clip.remove(request.name)
        like_b.r_clips -= 1
        like_b.save()
    else:
        like_b.r_clip.add(request.name)
        like_b.r_clips += 1
        like_b.save()
    return redirect('/r_detail/' + str(r_id))
