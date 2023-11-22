from django.urls import path
from my_blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from .forms import LoginForm

urlpatterns = [

  path('', views.home, name = 'home'),
  path('blog', views.Blogs.as_view(), name = 'blog'), 
  path('podcast', views.podcast, name = 'podcast'),
  path('contact', views.contact, name = 'contact'),
  path('post/<int:pk>', views.Post.as_view(), name = 'post'),
  path('create_post', views.MakePost.as_view(), name = 'create_post'),
  path('inner_page', views.inner_page, name = 'inner_page'),
  path('createpost2', views.createpost, name = 'createpost2')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)