from django.shortcuts import render
from django.http import HttpResponse


from .models import Post
from django.views import generic

# Create your views here.
def home(request):
    return HttpResponse("Hellow world")

# rendering html document
def article(request):
    return render(request,"article/article.html",{})


# rendering document with certian value
def index(request):
    context={
        "name":"Ram",
        "age": "10"
    }
    return render(request,"article/index.html",context)



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'article/article_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'article/article_detail.html'