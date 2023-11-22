from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Post as Postss, Category, Comment
# from .forms import CommentForm
from django.views.generic import ListView, DetailView, CreateView
from .forms import CreatePost
from django.contrib import messages


# Create your views here.
def home(request):
  return render(request, 'index.html', )

def blog(request):
  return render(request, 'blog.html', )

def podcast(request):
  return render(request, 'podcast.html', )

def contact(request):
  return render(request, 'contact.html', )


class Blogs(ListView):
  model = Postss
  template_name = 'blog.html'

class Post(DetailView):
  model = Postss
  template_name = 'post.html'  

class MakePost(CreateView):
  model = Postss
  template_name = 'create_post.html'
  fields = '__all__'


def createpost(request):
  if request.method == 'POST':
    form = CreatePost(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Your post was saved succesfully!')
      form = CreatePost()
    return render(request, 'blog.html')
  else:
    form = CreatePost()
    return render(request, 'create_post.html')


#   if data ==None:
#     all_post = Post.objects.all()
#   else:
#   single_post = Post.objects.all()[0]
#   return render(request, 'post.html', {'single_post': single_post})

def inner_page(request):
  return render(request, 'inner-page.html', )

# def post_detailview(request, id):

#   if request.method == 'POST':
#     cf = CommentForm(request.POST or None)
#     if cf.is_valid():
#       content = request.POST.get('content')
#       comment = Comment.objects.create(post = post, user = request.user, content = content)
#       comment.save()
#       return redirect(post.get_absolute_url())
#     else:
#       cf = CommentForm()
    
#     context ={
#     'comment_form':cf,
#     }
#     return render(request, 'post_detail.html', context)
