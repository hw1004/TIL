from django.shortcuts import render, redirect
# redirect는 강제적으로 특정 페이지로 넘어가게 하는 것

from .models import Article

# Create
def new(request):
    return render(request, 'board/new.html')

def create(request):   # 저장하는 과정
    title = request.GET['title']
    content = request.GET['content']  
    
    article = Article()
    
    article.title = title
    article.content = content
    article.save()
    
    return redirect(f'/board/{article.pk}/')

    
# Read
def index(request):
    # 모든 게시글 조회
    articles = Article.objects.all()
        
    return render(request, 'board/index.html', {
        'articles': articles,
    })

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/detail.html', {
        'article': article,
    })

# Update
def edit(request,pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/edit.html', {
        'article': article,
    })

def update(request, pk):
    article = Article.objects.get(pk=pk)
    title = request.GET['title']
    content = request.GET['content']
    article.title = title
    article.content = content
    article.save()
    return redirect(f'/board/{article.pk}/')

# Delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/board/')


# /board/new/ => new 함수 실행 => new.html return (사용자 글을 쓸 곳 - 내용 비워두기)
# /board/create/ => create 함수 실행 => 내용 비워놓기
# /board/ => index 함수 실행 => index.html return (글 목록)
# /board/<int:pk>/ => detail 함수 실행(pk는 변수 라우팅) => detail.html return (글 상세보기)
# /board/edit/ => edit 함수 실행 => edit.html return(글 수정할 곳)
# /board/update/ => update 함수 실행 => 내용 비워두기
# /board/delete/ => delete 함수 실행 => 내용 비워두기