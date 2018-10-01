from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Article
from .forms import PostForm
# Create your views here.


def postCreate(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
        "form":form,
    }
    return render(request, 'articleCreate.html',context)


def article_list(request):
    articles=Article.objects.all().order_by('date')
    return  render(request, 'article_list.html', { 'all_post' :articles })

def post_detail_view(request,id=None):
    instance=get_object_or_404(Article,id=id)
    context={
        "title" : instance.title,
        "instance":instance
    }
    # post = Article.objects.all()
    return render(request, 'articledetail.html', context)


# def home(request):
#     all_post=Post.objects.all()
#     return render(request, 'index.html', {'all_post_show':all_post})
