from django.shortcuts import render
from django.http import HttpResponse


from .models import Post
from django.views import generic

from .forms import AskQuestionForm

# Create your views here.
def home(request):
    return HttpResponse("Hellow world")

# rendering document with certian value
def index(request):
    context={
        "name":"Ram",
        "age": 10
    }
    return render(request,"article/index.html",context)


# contact page
def contact(request):
    return render(request,"article/contact.html",{})



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'article/article_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'article/article_detail.html'


def AskQuestionView(request):
    
    if request.method == "Get":
        form = AskQuestionForm()
    else:

        form = AskQuestionForm(request.POST)

        if form.is_valid():
            form.save()

            form = AskQuestionForm()
            return render(request,"article/ask_question.html",{'form':form,"success":"Message sent successfully!"})
    
    return render(request, "article/ask_question.html", {'form': form})