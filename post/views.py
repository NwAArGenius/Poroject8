from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def home(request):
    article = Article.objects.all()
    paginator = Paginator(article,4)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context= {'pages_obj':page_obj}
    return render(request,'home.html',context)


def list_post(request):
    listes=Article.objects.all()
    paginator = Paginator(listes,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request , 'listes_articles.html', context)


def details(request,id):
    article = Article.objects.get(id=id)
    context = {'article':article}
    return render(request,'details.html', context)


def createArticle(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST or None)
        if form.is_valid():
          form.save()
        return redirect('listes_articles')  
    context = {'form':form} 
    return render(request, 'create.html',context)



def update(request,id):
    article = Article.objects.get(id=id) 
    form = ArticleForm(instance=article) 
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('/')  
    context= {'form':form}
    return render(request,'update.html',context)




def apropos(request):
   return render(request,'apropos.html')



def contact(request):
    return render(request ,'contact.html')